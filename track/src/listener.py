#!/usr/bin/env python3
from turtle import position
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from sol_msg.msg import track
from geometry_msgs.msg import Twist

def callback(data):
    # rospy.loginfo(data)
    # rospy.loginfo(data.position[0])


    if data.position[0] <260:
        rospy.loginfo('turn left')
        cmd(0, 0.1) 

    elif data.position[0] <410:
        rospy.loginfo('go')
        cmd(0.1, 0)
   
    else:
        rospy.loginfo('turn right')
        cmd(0, -0.1)


def callback2(data):
    if data.data:
        listener()
        
    else:
        cmd(0,0)
        rospy.sleep(5)


def list():
    # stop 토픽 받는 함수 생성
    rospy.Subscriber('stop', Bool, callback2)
    rospy.spin()


def listener():
    rospy.Subscriber('tracker', track, callback)
    pub_array = track()
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
    rospy.init_node('listener')
    list()