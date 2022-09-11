#!/usr/bin/env python3
from turtle import position
import rospy

from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from sol_msg.msg import track


def talker():
    y=0
    t_num=0
    size=0
    pub = rospy.Publisher('tracker', track, queue_size=1)
    rate = rospy.Rate(10)
    pub_array = track()
    cnt=1
    while not rospy.is_shutdown():
        
        if cnt<=10:
            x=100
        elif cnt<=20:
            x=350
        elif cnt<=30:
            x=500
        if cnt==30:
            cnt=1
        cnt+=1
        pub_array.position=[]      
        pub_array.position.append(x)
        pub_array.position.append(y)
        pub_array.position.append(size)
        pub_array.position.append(t_num)
        pub.publish(pub_array)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('pubtracker')
    talker()