cmake_minimum_required(VERSION 3.8)
project(task_1_cpu_temp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# Publisher
add_executable(publisher_node src/pub_node.cpp)
ament_target_dependencies(publisher_node rclcpp std_msgs)

# Subscriber
add_executable(subscriber_node src/sub_node.cpp)
ament_target_dependencies(subscriber_node rclcpp std_msgs)

install(TARGETS
  publisher_node
  subscriber_node
  DESTINATION lib/${PROJECT_NAME})
  
ament_package()
