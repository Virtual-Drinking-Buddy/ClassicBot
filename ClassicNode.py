#!/usr/bin/env python3

## Summary: This code will distribute the commands from the GUInode to the arduino
##
import serial
import time
import rospy
from std_msgs.msg import Int16, Int16MultiArray

done = False


# Need to update this to read in a vector from the computer running user inputs
def callback_number(msg):
    global dat
    dat = msg.data

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    rospy.init_node('ClassicNode')

    sub = rospy.Subscriber("/GUINode", Int16, callback_number)

    rate = rospy.Rate(1000)
    # Now we start the real code for control of the vehicle
    while not rospy.is_shutdown() and not done:
        # Delete this when sending full user data is working
        ser.write(str(dat).encode('utf-8'))
        # msg = Int16MultiArray()
        # msg.data = pub_array
        # pub.publish(msg)
        # rate.sleep()