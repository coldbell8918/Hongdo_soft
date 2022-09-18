#!/usr/bin/env python3
from ast import Global
from turtle import position
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from sol_msg.msg import track
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from track.srv import PlaySong, PlaySongResponse
import os


stop = 1
cnt=0

def tracker_callback(data):
    global cnt
    play_song_client(1)
    if (stop):
        rospy.loginfo('stop')
        cmd(0, 0)
    else:
        if data.position[0] <260:
            rospy.loginfo('turn right')
            cmd(0, 0.2) 

        elif data.position[0] <410:
            rospy.loginfo('go')
            cmd(0.2, 0)
    
        else:
            rospy.loginfo('turn left')
<<<<<<< HEAD
            cmd(0, -0.2)
=======
            cmd(0, -0.1)
    cnt+=1
    if cnt==1000:
        cnt=0



def play_song_client(number):
    rospy.wait_for_service('play_voice')
    try:
        play_song = rospy.ServiceProxy('play_voice',PlaySong)
        return play_song(number)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
>>>>>>> 512ff3f0cd1087654c765f70c757586bb2b3894a


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