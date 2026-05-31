#include <cstdio>
#include <cmath>
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "turtlesim/msg/pose.hpp"
#include "std_srvs/srv/empty.hpp"


using namespace std::chrono_literals;

class PatrolController : public rclcpp::Node
{
public:

  PatrolController()
  : Node("patrol_controller")
  {

    this->declare_parameter("linear_speed", 2.0);
    this->declare_parameter("angular_speed", 2.0);

    // log to terminal to verify parameters are loaded correctly
    RCLCPP_INFO(this->get_logger(), "linear_speed: %.2f", this->get_parameter("linear_speed").as_double());
    RCLCPP_INFO(this->get_logger(), "angular_speed: %.2f", this->get_parameter("angular_speed").as_double());


    publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
    stop_service_ = this->create_service<std_srvs::srv::Empty>(
      "/stop", std::bind(&PatrolController::stop_handler, this, std::placeholders::_1, std::placeholders::_2));
    
    continue_service_ = this->create_service<std_srvs::srv::Empty>(
      "/continue", std::bind(&PatrolController::continue_handler, this, std::placeholders::_1, std::placeholders::_2));

    timer_ = this->create_wall_timer(100ms, [this]() {
     if (!is_running) {
        return;
      }
      lin_speed = this->get_parameter("linear_speed").as_double();
      ang_speed = this->get_parameter("angular_speed").as_double();

      msg_.linear.x = lin_speed;
      msg_.angular.z = ang_speed;
      publisher_->publish(msg_);
    });
  }

private:
  void stop_handler(const std_srvs::srv::Empty::Request::SharedPtr req, const std_srvs::srv::Empty::Response::SharedPtr res)
  {
    (void)req;
    (void)res;
    is_running = false;
    msg_.linear.x = 0.0;
    msg_.angular.z = 0.0;
    publisher_->publish(msg_);}

  void continue_handler(const std_srvs::srv::Empty::Request::SharedPtr req, const std_srvs::srv::Empty::Response::SharedPtr res)
  {
    (void)req;
    (void)res;
    is_running = true;
    msg_.linear.x = lin_speed;
    msg_.angular.z = ang_speed;
    publisher_->publish(msg_);
  }


  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
  rclcpp::Service<std_srvs::srv::Empty>::SharedPtr stop_service_;
  rclcpp::Service<std_srvs::srv::Empty>::SharedPtr continue_service_;
  geometry_msgs::msg::Twist msg_;
  double lin_speed;
  double ang_speed;
  rclcpp::TimerBase::SharedPtr timer_;
  bool is_running = true;
};

int main(int argc, char ** argv)
{

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PatrolController>());
  rclcpp::shutdown();

  return 0;
}
