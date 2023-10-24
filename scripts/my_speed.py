#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

if __name__=='__main__':
    rospy.init_node("velocity_goal")

    pub= rospy.Publisher("/virtual_dc_motor_controller/set_velocity_goal", Float32, queue_size=1)
    while not rospy.is_shutdown():
        pub.publish(-100)