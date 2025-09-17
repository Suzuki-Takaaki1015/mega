import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    static_tf_publisher_lidar = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=[
            '--x', '0.0',
            '--y', '0.0',
            '--z', '0.0',
            '--roll', '-1.57',
            '--pitch', '-1.57',
            '--yaw', '0.0',
            '--frame-id', 'UTM_30LX',
            '--child-frame-id', 'UTM_30LX_corrected'
        ]
    )

    return LaunchDescription([
        static_tf_publisher_lidar,
    ])