#!/usr/bin/env python3

## Summary: This code will distribute the commands from the GUInode to the arduino
##
import serial
import time
import numpy as np
import rospy
from std_msgs.msg import Int16, Int16MultiArray

command_msg = 0
i = 0

done = False
test = 0

# Need to update this to read in a vector from the computer running user inputs
def callback_number(msg):
    global command_msg
    dat = msg.data
    command_msg = dat[0]

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    rospy.init_node('ClassicNode')

    sub = rospy.Subscriber("/ClassicTopic", Int16MultiArray, callback_number)

    rate = rospy.Rate(1000)
    # Now we start the real code for control of the vehicle
    while not rospy.is_shutdown() and not done:
        # Delete this when sending full user data is working
        ser.write(str(dat).encode('utf-8'))
        # msg = Int16MultiArray()
        # msg.data = pub_array
        # pub.publish(msg)
        # rate.sleep()

        print(command_msg)


        # save = command_msg

