cmake_minimum_required(VERSION 3.8)
project(lab2_turtle_mover)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(turtlesim REQUIRED)

add_executable(status_publisher src/status_publisher.cpp)
add_executable(patrol_controller src/patrol_controller.cpp)


target_include_directories(status_publisher PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include/${PROJECT_NAME}>)
  
target_include_directories(patrol_controller PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include/${PROJECT_NAME}>)


set(msg_files
  "msg/RobotStatus.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  DEPENDENCIES
    geometry_msgs
    std_msgs
)

rosidl_get_typesupport_target(cpp_typesupport_target
  ${PROJECT_NAME}
  "rosidl_typesupport_cpp"
)

target_link_libraries(status_publisher
  ${cpp_typesupport_target}
)
ament_export_dependencies(rosidl_default_runtime)
ament_target_dependencies(
  status_publisher
  "rclcpp"
  "geometry_msgs"
  "std_msgs"
  "std_srvs"
  "turtlesim"
)
  
ament_target_dependencies(
  patrol_controller
  "rclcpp"
  "geometry_msgs"
  "std_msgs"
  "std_srvs"
  "turtlesim"
)

install(TARGETS status_publisher
  DESTINATION lib/${PROJECT_NAME})

install(TARGETS patrol_controller
DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY params
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
