#!/usr/bin/env python3

## Summary: This code is used to create a GUI for the user to control the ClassicBot. These controls are then sent over
##          ROS to the RaspberryPI where they can be then manipulated and sent to the arduino for hardware control.

import numpy as np
import rospy
from std_msgs.msg import Int16, Int16MultiArray

# Here you can put any of your initialization code

if __name__ == '__main__':

    rospy.init_node("GUI_Node")

    pub = rospy.Publisher("/ClassicNode", Int16MultiArray, queue_size=10)
    rate = rospy.Rate(1000)

    while not rospy.is_shutdown():
        # Any road that needs to be constantly running can go here. This will just stop the code if there is a
        # disconnect from the ROS network.




        # Publishing data to User Topic
        ## We can write whatever values we want to each of these variables and they will be send to the Raspi.
        pub_array = np.array([Value0, Value1, Value2, Value3, Value4, Value5, Value6, Value7])
        msg = Int16MultiArray()
        msg.data = pub_array
        pub.publish(msg)
        rate.sleep()