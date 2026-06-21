"""
nav2_simulation.launch.py
--------------------------
Thin wrapper around nav2_bringup's tb3_simulation_launch.py.

We only override:
  - params_file  →  our editable config/nav2_params.yaml
  - map          →  nav2_bringup's built-in tb3_sandbox map (can be overridden on CLI)

Everything else (world, robot SDF, Gazebo, RViz) is handled by the upstream
tb3_simulation_launch.py so we don't have to maintain it.

Usage:
  ros2 launch my_robot_nav2 nav2_simulation.launch.py
  ros2 launch my_robot_nav2 nav2_simulation.launch.py slam:=True
  ros2 launch my_robot_nav2 nav2_simulation.launch.py map:=/path/to/my_map.yaml
  ros2 launch my_robot_nav2 nav2_simulation.launch.py headless:=False   # open Gazebo GUI
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

    # ------------------------------------------------------------------
    # Our editable params file — edit this to tune Nav2 behaviour
    # ------------------------------------------------------------------
    default_params_file = os.path.join(pkg_my_nav2, 'config', 'nav2_params.yaml')

    # Default map shipped with nav2_bringup (TurtleBot3 sandbox world)
    default_map = os.path.join(pkg_nav2_bringup, 'maps', 'tb3_sandbox.yaml')

    # ------------------------------------------------------------------
    # Expose arguments so they can still be overridden from the CLI
    # ------------------------------------------------------------------
    declare_params_file = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_file,
        description='Full path to the Nav2 params yaml. '
                    'Edit my_robot_nav2/config/nav2_params.yaml to customise.'
    )

    declare_map = DeclareLaunchArgument(
        'map',
        default_value=default_map,
        description='Full path to map yaml file. '
                    'Use map_saver_cli to save a new map into my_robot_nav2/maps/.'
    )

    declare_slam = DeclareLaunchArgument(
        'slam',
        default_value='False',
        description='Set to True to run SLAM instead of loading a pre-built map.'
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
    # Delegate to the upstream tb3 simulation launch, injecting our params
    # ------------------------------------------------------------------
    nav2_tb3_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_nav2_bringup, 'launch', 'tb3_simulation_launch.py')
        ),
        launch_arguments={
            'params_file': LaunchConfiguration('params_file'),
            'map':         LaunchConfiguration('map'),
            'slam':        LaunchConfiguration('slam'),
            'headless':    LaunchConfiguration('headless'),
            'use_rviz':    LaunchConfiguration('use_rviz'),
        }.items()
    )

    return LaunchDescription([
        declare_params_file,
        declare_map,
        declare_slam,
        declare_headless,
        declare_use_rviz,
        nav2_tb3_sim,
    ])
