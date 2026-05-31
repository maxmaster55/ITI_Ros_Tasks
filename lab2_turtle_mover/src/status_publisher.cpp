#include <cstdio>
#include <cmath>
#include "rclcpp/rclcpp.hpp"
#include "lab2_turtle_mover/msg/robot_status.hpp"
#include "turtlesim/msg/pose.hpp"


using namespace std::chrono_literals;

class StatusPublisher : public rclcpp::Node
{
public:

  StatusPublisher()
  : Node("status_publisher")
  {

    this->declare_parameter("status_rate", 2.0);


    int timer_rate = this->get_parameter("status_rate").as_double();
    auto timer_period = std::chrono::duration<float>(1.0 / timer_rate);

    publisher_ = this->create_publisher<lab2_turtle_mover::msg::RobotStatus>("/robot/status", 10);
    subscription_ = this->create_subscription<turtlesim::msg::Pose>(
      "/turtle1/pose", 10, std::bind(&StatusPublisher::pose_callback, this, std::placeholders::_1));

    timer_ = this->create_wall_timer(timer_period, std::bind(&StatusPublisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
    RCLCPP_INFO(this->get_logger(), "sending robot status: state=%s, temperature=%.2f, lap_count=%d", status_msg_.state.c_str(), status_msg_.temperature, status_msg_.lap_count);
    publisher_->publish(status_msg_);
  }

  void pose_callback(const turtlesim::msg::Pose::SharedPtr msg)
  {
    RCLCPP_INFO(this->get_logger(), "Received pose: x=%.2f, y=%.2f, theta=%.2f", msg->x, msg->y, msg->theta);
    status_msg_.pose.x = msg->x;
    status_msg_.pose.y = msg->y;
    status_msg_.pose.theta = msg->theta;
    if (msg->linear_velocity != 0.0){
      status_msg_.state = "running";
      status_msg_.temperature = 25.0f + (msg->linear_velocity * 5.0f);
    }
    else {
      status_msg_.state = "stopped";
      status_msg_.temperature = 25.0f;
    }

    constexpr float TWO_PI = 2.0f * 3.141f;
    if (first_pose_received_) {
      float delta_theta = msg->theta - prev_theta_;
      if (delta_theta > 3.141f) {
        delta_theta -= TWO_PI;
      } else if (delta_theta < -3.14f) {
        delta_theta += TWO_PI;
      }

      theta_accumulated_ += std::fabs(delta_theta);
      status_msg_.lap_count = static_cast<int>(theta_accumulated_ / TWO_PI);
    } else {
      first_pose_received_ = true;
    }
    prev_theta_ = msg->theta;
  }

  rclcpp::Publisher<lab2_turtle_mover::msg::RobotStatus>::SharedPtr publisher_;
  rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscription_;
  
  rclcpp::TimerBase::SharedPtr timer_;
  lab2_turtle_mover::msg::RobotStatus status_msg_;
  float prev_theta_ = 0.0f;
  float theta_accumulated_ = 0.0f;
  bool first_pose_received_ = false;
};

int main(int argc, char ** argv)
{

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<StatusPublisher>());
  rclcpp::shutdown();

  return 0;
}
