# launch/topic_examples.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='task_1_cpu_temp',
            executable='publisher_node',
            name='minimal_publisher',
            output='screen',
        ),
        Node(
            package='task_1_cpu_temp',
            executable='subscriber_node',
            name='minimal_subscriber',
            output='screen',
        ),
    ])