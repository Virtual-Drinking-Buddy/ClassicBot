#!/usr/bin/env python3

## Summary: This code is used to create a GUI for the user to control the ClassicBot. These controls are then sent over
##          ROS to the RaspberryPI where they can be then manipulated and sent to the arduino for hardware control.

# import numpy as np
import rospy
import wx
from std_msgs.msg import Int16, Int16MultiArray

# Here you can put any of your initialization code
global msg

# AddGUI widget code here
def onButton1(event):
    print "1"
    msg = 1
    pub.publish(msg)
    rate.sleep()
def onButton2(event):
    print "2"
    msg = 2
    pub.publish(msg)
    rate.sleep()
def onButton3(event):
    print "3"
    msg = 3
    pub.publish(msg)
    rate.sleep()
def onButton4(event):
    print "4"
    msg = 4
    pub.publish(msg)
    rate.sleep()
def onButton5(event):
    print "5"
    msg = 5
    pub.publish(msg)
    rate.sleep()
def onButton6(event):
    print "6"
    msg = 6
    pub.publish(msg)
    rate.sleep()
def onButton7(event):
    print "7"
    msg = 7
    pub.publish(msg)
    rate.sleep()

# Set up window
app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,500,500)

panel = wx.Panel(frame, wx.ID_ANY)

#Buttons
forward1 = wx.Button(panel, wx.ID_ANY, 'Forward', (105, 10))
forward1.Bind(wx.EVT_BUTTON, onButton1)
backward2 = wx.Button(panel, wx.ID_ANY, 'Backward', (105, 200))
backward2.Bind(wx.EVT_BUTTON, onButton2)
right3 = wx.Button(panel, wx.ID_ANY, 'Right', (200, 105))
right3.Bind(wx.EVT_BUTTON, onButton3)
left4 = wx.Button(panel, wx.ID_ANY, 'Left', (10, 105))
left4.Bind(wx.EVT_BUTTON, onButton4)
launch5 = wx.Button(panel, wx.ID_ANY, 'Launch', (105, 105))
launch5.Bind(wx.EVT_BUTTON, onButton5)
inc_speed6 = wx.Button(panel, wx.ID_ANY, '+ Speed', (300, 50))
inc_speed6.Bind(wx.EVT_BUTTON, onButton6)
dec_speed7 = wx.Button(panel, wx.ID_ANY, '- Speed', (300, 150))
dec_speed7.Bind(wx.EVT_BUTTON, onButton7)

#Show window
# frame.Show()
# frame.Centre()
# app.MainLoop()

if __name__ == '__main__':

    rospy.init_node("GUI_Node")

    pub = rospy.Publisher("/ClassicNode", Int16, queue_size=10)
    rate = rospy.Rate(1000)

    while not rospy.is_shutdown():
        # Any road that needs to be constantly running can go here. This will just stop the code if there is a
        # disconnect from the ROS network.
        # Show window
        frame.Show()
        frame.Centre()
        app.MainLoop()
        # msg = input("Please enter a number 1-7 here:/n")

        # Publishing data to User Topic
        ## We can write whatever values we want to each of these variables and they will be send to the Raspi.
        # pub_array = np.array([Value0, Value1, Value2, Value3, Value4, Value5, Value6, Value7])
        # msg = Int16MultiArray()
        # msg.data = pub_array
        pub.publish(msg)
        rate.sleep()