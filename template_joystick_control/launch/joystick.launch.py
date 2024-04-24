#!/usr/bin/env python3

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from tmr4243_utilities.utilities import anon


def generate_launch_description():

    arg_param_file = launch.actions.DeclareLaunchArgument(
        'param_file',
        default_value=launch.substitutions.PathJoinSubstitution(
            [launch_ros.substitutions.FindPackageShare('template_joystick_control'), 'config', 'param.yaml']
        )
    )

    arg_task = launch.actions.DeclareLaunchArgument(
        'task',
        default_value=launch.substitutions.TextSubstitution(text='simple'),
        description='Joystick control task type. Choose between simple, basin, and body.',
        choices=['simple', 'basin', 'body']
    )

    node_joystick_control = launch_ros.actions.Node(
        package='template_joystick_control',
        executable='joystick_control_node.py',
        name=f'{anon()}joystick_control',
        parameters=[
                {'task': launch.substitutions.LaunchConfiguration('task')},
        ],
        output='screen'
    )

    node_joy = launch_ros.actions.Node(
        package='joy',
        executable='joy_node',
        name=f"{anon()}joy_node",
    )

    return launch.LaunchDescription([
        arg_task,
        arg_param_file,
        node_joystick_control,
        node_joy
    ])
