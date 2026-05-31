cmake_minimum_required(VERSION 3.8)
project(say_hi_service)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

add_executable(say_hi_service src/say_hi_service.cpp)
add_executable(say_hi_client src/say_hi_client.cpp)


ament_target_dependencies(
  say_hi_service
  "rclcpp"
  "example_interfaces"
)

ament_target_dependencies(
  say_hi_client
  "rclcpp"
  "example_interfaces"
)

install(TARGETS say_hi_service
  DESTINATION lib/${PROJECT_NAME})

install(TARGETS say_hi_client
  DESTINATION lib/${PROJECT_NAME})
  
ament_package()
