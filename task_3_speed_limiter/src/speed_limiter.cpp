#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <cstdlib>
#include <rclcpp/publisher.hpp>
#include "math.h"

class SpeedLimiter : public rclcpp::Node
{
public:
  SpeedLimiter() : Node("speed_limiter")
  {
    RCLCPP_INFO(this->get_logger(), "Speed Limiter Node has been started.");
    speed_sub_ = this->create_subscription<geometry_msgs::msg::Twist>(
      "/cmd_vel", 10, std::bind(&SpeedLimiter::topic_callback, this, std::placeholders::_1));
    speed_pub_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel_limited", 10);
  }


private:
  void topic_callback(const geometry_msgs::msg::Twist::SharedPtr msg)
  {
    RCLCPP_INFO(this->get_logger(), "got x velocity: %f & x angular: %f", msg->linear.x, msg->angular.z);

    if (abs(msg->linear.x) > 1.0) {
      RCLCPP_WARN(this->get_logger(), "Linear velocity is too high! Limiting to 1 m/s.");
      msg->linear.x = 1.0;
    }
    if (abs(msg->angular.z) > 1.0) {
      RCLCPP_WARN(this->get_logger(), "Angular velocity is too high! Limiting to 1 rad/s.");
      msg->angular.z = 1.0;
    }
    speed_pub_->publish(*msg);
  }


  rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr speed_sub_;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr speed_pub_;
};


int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SpeedLimiter>();
  rclcpp::spin(node);
  rclcpp::shutdown();

  return 0;
}
