cmake_minimum_required(VERSION 3.8)
project(my_robot_nav2)

find_package(ament_cmake REQUIRED)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install config files (nav2_params.yaml, rviz config)
install(DIRECTORY config/
  DESTINATION share/${PROJECT_NAME}/config
)

# Install maps directory (pre-built maps go here)
install(DIRECTORY maps/
  DESTINATION share/${PROJECT_NAME}/maps
)

ament_package()
