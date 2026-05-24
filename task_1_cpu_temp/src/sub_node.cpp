#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"
#include <rclcpp/node.hpp>

using namespace std::chrono_literals;

class Float32Subscriber : public rclcpp::Node{
public:
  Float32Subscriber() : Node("temp_subscriber"){
    subscription_ = this->create_subscription<std_msgs::msg::Float32>(
      "temp_sensor_topic",
      10,
      std::bind(&Float32Subscriber::topic_callback, this, std::placeholders::_1)
    );
  }

private:
  void topic_callback(const std_msgs::msg::Float32::SharedPtr msg){
    RCLCPP_INFO(this->get_logger(), "Received: %f", msg->data);
  }

  rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr subscription_;
};

int main(int argc, char * argv[]){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Float32Subscriber>());
  rclcpp::shutdown();

  return 0;
}

