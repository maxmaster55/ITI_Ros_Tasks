#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"
#include <rclcpp/node.hpp>
#include <fstream>
#include <string>

using namespace std::chrono_literals;

class Float32Publisher : public rclcpp::Node{
public:
  Float32Publisher() : Node("temp_publisher"), count_(0){

    file_.open("/sys/class/thermal/thermal_zone1/temp");
    if (!file_.is_open()) {
      RCLCPP_ERROR(this->get_logger(), "Failed to open the file.");
    }
    publisher_ = this->create_publisher<std_msgs::msg::Float32>("temp_sensor_topic", 10);
    timer_ = this->create_wall_timer(
      1s,
      std::bind(&Float32Publisher::timer_callback, this)
    );
  }

private:
  void timer_callback(){

    std::string line;
    file_.seekg(0);
    file_ >> line;

    count_ = std::stoi(line);

    auto msg = std_msgs::msg::Float32();
    msg.data = count_/1000; // Convert to Celsius
    RCLCPP_INFO(this->get_logger(), "Publishing temp:%f", msg.data);
    publisher_->publish(msg);
    count_++;
  }


  rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  std::ifstream file_;
  int count_;
};

int main(int argc, char * argv[]){
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Float32Publisher>());
  rclcpp::shutdown();

  return 0;
}