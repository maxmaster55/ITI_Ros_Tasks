"""
slam.launch.py
--------------
Thin wrapper around nav2_bringup's slam_launch.py.

Runs SLAM (slam_toolbox) on top of the TurtleBot3 simulation.
Drive the robot with teleop, then save the map with:

    ros2 run nav2_map_server map_saver_cli -f ~/00_Software/src/my_robot_nav2/maps/my_map

Usage:
  ros2 launch my_robot_nav2 slam.launch.py
  ros2 launch my_robot_nav2 slam.launch.py headless:=False   # open Gazebo GUI
"""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------
    pkg_nav2_bringup = get_package_share_directory('nav2_bringup')
    pkg_my_nav2      = get_package_share_directory('my_robot_nav2')

    default_params_file = os.path.join(pkg_my_nav2, 'config', 'nav2_params.yaml')

    # ------------------------------------------------------------------
    # Arguments
    # ------------------------------------------------------------------
    declare_params_file = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_file,
        description='Full path to the Nav2 params yaml.'
    )

    declare_headless = DeclareLaunchArgument(
        'headless',
        default_value='True',
        description='Set to False to open the Gazebo GUI (gzclient).'
    )

    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='True',
        description='Set to False to skip launching RViz.'
    )

    # ------------------------------------------------------------------
    # Start the TB3 simulation with slam:=True via tb3_simulation_launch
    # ------------------------------------------------------------------
    slam_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'tb3_simulation_launch.py')
        ),
        launch_arguments={
            'slam':        'True',
            'params_file': LaunchConfiguration('params_file'),
            'headless':    LaunchConfiguration('headless'),
            'use_rviz':    LaunchConfiguration('use_rviz'),
        }.items()
    )

    return LaunchDescription([
        declare_params_file,
        declare_headless,
        declare_use_rviz,
        slam_sim,
    ])
