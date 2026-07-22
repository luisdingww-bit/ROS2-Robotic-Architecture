# robot_launch.py
"""ROS2 launch file template for robotic fabrication."""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Robot arm controller
        Node(
            package="ur_robot_driver",
            executable="ur_control_node",
            name="robot_controller",
            parameters=["config/robot_config.yaml"],
        ),
        
        # Toolpath executor
        Node(
            package="robotic_fabrication",
            executable="toolpath_executor",
            name="toolpath_executor",
            parameters=["config/toolpath_config.yaml"],
        ),
        
        # Vision system
        Node(
            package="realsense_ros",
            executable="realsense_node",
            name="vision_node",
        ),
        
        # Fabrication monitor
        Node(
            package="robotic_fabrication",
            executable="fabrication_monitor",
            name="fabrication_monitor",
        ),
    ])
