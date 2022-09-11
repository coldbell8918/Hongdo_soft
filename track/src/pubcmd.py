#!/usr/bin/env python3
from turtle import position
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from sol_msg.msg import track
from geometry_msgs.msg import Twist

stop = 1

def tracker_callback(data):
    if (stop):
        rospy.loginfo('stop')
        cmd(0, 0)
    else:
        if data.position[0] <260:
            rospy.loginfo('turn right')
            cmd(0, 0.1) 

        elif data.position[0] <410:
            rospy.loginfo('go')
            cmd(0.1, 0)
    
        else:
            rospy.loginfo('turn left')
            cmd(0, -0.1)


def stop_callback(data):
    global stop
    if data.data == True:
        stop = 1
    else:
        stop = 0
        


def init():
    rospy.Subscriber('stop', Bool, stop_callback)
    rospy.Subscriber('tracker', track, tracker_callback)
    rospy.spin()


def cmd(linear, angular):
    pub=rospy.Publisher("cmd_vel", Twist, queue_size=10)

    cmd_msg=Twist()
    cmd_msg.linear.x=linear
    cmd_msg.linear.y=0
    cmd_msg.linear.z=0
    cmd_msg.angular.x=0
    cmd_msg.angular.y=0
    cmd_msg.angular.z=angular
    pub.publish(cmd_msg)
    
if __name__ == '__main__':
    rospy.init_node('pubcmd', anonymous=True)
    init()