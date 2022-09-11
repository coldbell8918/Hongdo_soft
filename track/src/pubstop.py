#!/usr/bin/env python3
from turtle import position
import rospy

from std_msgs.msg import Float64MultiArray  
from std_msgs.msg import Bool
from sol_msg.msg import track


def talker():
    pub = rospy.Publisher('stop', Bool, queue_size=1)
    rate = rospy.Rate(10)
    cnt =1
    while not rospy.is_shutdown():
        if cnt <=25:
            x=1
        elif cnt <=50:
            x=0
        if cnt ==50:
            cnt=1
        cnt+=1
        pub.publish(x)
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('pubstop')
    talker()