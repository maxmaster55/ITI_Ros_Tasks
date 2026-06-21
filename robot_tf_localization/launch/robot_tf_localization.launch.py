from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    config = os.path.join(
        get_package_share_directory('robot_tf_localization'),
        'config',
        'ekf.yaml'
    )



    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation time'
        ),

        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node_odom',
            output='screen',
            parameters=[config],
            # remappings=[
            #     ('odometry/filtered', 'odometry/local'),
            #     ('set_pose', 'initialpose')
            # ]
        ),
        # Transform 1: odom -> base_footprint
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.0',
                '--y', '0.0',
                '--z', '0.0',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '0.0',
                '--frame-id', 'odom',
                '--child-frame-id', 'base_footprint'
            ],
            name='odom_to_base_footprint_broadcaster'
        ),
        # Transform 2: base_footprint -> base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.0',
                '--y', '0.0',
                '--z', '0.05',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '0.0',
                '--frame-id', 'base_footprint',
                '--child-frame-id', 'base_link'
            ],
            name='base_footprint_to_base_link_broadcaster'
        ),
        # Transforms 3: base_link -> imu_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.5',
                '--y', '-0.1',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '0.0',
                '--frame-id', 'base_link',
                '--child-frame-id', 'imu_link'
            ],
            name='base_link_to_imu_broadcaster'
        ),
        # Transforms 3: base_link -> gps_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.2',
                '--y', '0.0',
                '--z', '0.25',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '0.0',
                '--frame-id', 'base_link',
                '--child-frame-id', 'gps_link'
            ],
            name='base_link_to_gps_broadcaster'
        ),
# ----------------------------- Ultrasonics -------------------------------------- #
        # Transforms 3: base_link -> ultrasonic1_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.5',
                '--y', '0.15',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '0.785398',
                '--frame-id', 'base_link',
                '--child-frame-id', 'ultrasonic1_link'
            ],
            name='base_link_to_ultrasonic1_link_broadcaster'
        ),
        # Transforms 3: base_link -> ultrasonic2_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.5',
                '--y', '0.0',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '0.0',
                '--frame-id', 'base_link',
                '--child-frame-id', 'ultrasonic2_link'
            ],
            name='base_link_to_ultrasonic2_link_broadcaster'
        ),    
        # Transforms 3: base_link -> ultrasonic3_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '0.5',
                '--y', '-0.15',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '-0.785398',
                '--frame-id', 'base_link',
                '--child-frame-id', 'ultrasonic3_link'
            ],
            name='base_link_to_ultrasonic3_link_broadcaster'
        ),    
        # Transforms 3: base_link -> ultrasonic4_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '-0.1',
                '--y', '0.15',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '2.35619',
                '--frame-id', 'base_link',
                '--child-frame-id', 'ultrasonic4_link'
            ],
            name='base_link_to_ultrasonic4_link_broadcaster'
        ),    
        # Transforms 3: base_link -> ultrasonic5_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '-0.1',
                '--y', '0.0',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '3.14159',
                '--frame-id', 'base_link',
                '--child-frame-id', 'ultrasonic5_link'
            ],
            name='base_link_to_ultrasonic5_link_broadcaster'
        ),    
        # Transforms 3: base_link -> ultrasonic6_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '--x', '-0.1',
                '--y', '-0.15',
                '--z', '0.1',
                '--roll', '0.0',
                '--pitch', '0.0',
                '--yaw', '-2.35619',
                '--frame-id', 'base_link',
                '--child-frame-id', 'ultrasonic6_link'
            ],
            name='base_link_to_ultrasonic6_link_broadcaster'
        ),    

    ])
