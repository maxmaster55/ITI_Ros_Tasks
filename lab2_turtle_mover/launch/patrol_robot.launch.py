# launch/topic_examples.launch.py
import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():
    param_file = os.path.join(
    get_package_share_directory('lab2_turtle_mover'),
    'params',
    'patrol_params.yaml'
    )
    return LaunchDescription([
        Node(
            package='lab2_turtle_mover',
            executable='status_publisher',
            name='status_publisher',
            output='screen',
            parameters=[param_file]
        ),
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
            output='screen',
            parameters=[param_file]
        ),
        Node(
            package='lab2_turtle_mover',
            executable='patrol_controller',
            name='patrol_controller',
            output='screen',
            parameters=[param_file]
        ),
    ])