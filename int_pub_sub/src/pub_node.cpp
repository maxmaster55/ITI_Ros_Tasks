#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include <rclcpp/node.hpp>

using namespace std::chrono_literals;

class IntPublisher : public rclcpp::Node{
public:
  IntPublisher() : Node("int_publisher"), count_(0){
    publisher_ = this->create_publisher<std_msgs::msg::Int32>("int_topic", 10);
    timer_ = this->create_wall_timer(
      100ms,
      std::bind(&IntPublisher::timer_callback, this)
    );
  }

private:
  void timer_callback(){
    auto msg = std_msgs::msg::Int32();
    msg.data = count_;
    RCLCPP_INFO(this->get_logger(), "Publishing: %d", msg.data);
    publisher_->publish(msg);
    count_++;
  }


  rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  int count_;
};

int main(int argc, char * argv[]){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<IntPublisher>());
  rclcpp::shutdown();

  return 0;
}