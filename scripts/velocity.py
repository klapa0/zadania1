#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import Float32

previous_time=1
previous_msg=UInt16()


def pose_callback(msg):
   global previous_msg
   global previous_time
   time_now=rospy.get_time()
   if((abs(msg.data-previous_msg.data))<3000):
       RPM=60*(msg.data-previous_msg.data)/(time_now-previous_time)/4096
   elif (msg.data-previous_msg.data>3000):
        RPM=60*(msg.data-previous_msg.data-4096)/(time_now-previous_time)/4096 
   else:
        RPM=60*(4096+msg.data-previous_msg.data)/(time_now-previous_time)/4096
   previous_time=time_now
   previous_msg=msg
   pub.publish(RPM)

if __name__=='__main__':
    rospy.init_node("velocity_speed")
    sub= rospy.Subscriber("/virtual_dc_motor/get_position", UInt16, callback=pose_callback)
    pub= rospy.Publisher("/virtual_dc_motor_driver/get_velocity", Float32, queue_size=1)

    rospy.loginfo("Node has been started")
    rospy.spin()