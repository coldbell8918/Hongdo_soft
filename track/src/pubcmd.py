#!/usr/bin/env python3

import rospy 
from std_msgs.msg import Bool
from sol_msg.msg import track
from geometry_msgs.msg import Twist

class human_tracker():
    def __init__(self):
        self.stop = True
        self.subs1=[]
        self.subs2=[]
        self.pubs=[]
        self.subs1.append(rospy.Subscriber('stop', Bool, self.stop_callback))
        self.subs2.append(rospy.Subscriber('tracker', track, self.tracker_callback))
        self.pubs['cmd_vel'] = rospy.Publisher("cmd_vel", Twist,queue_size=1)

    def stop_callback(self, data):
        if data.data == True:
            self.stop=True
        else:
            self.stop = False

    def tracker_callback(self, data):
        if self.stop: return
        
        if data.position[0] <260:
            rospy.loginfo('turn right')
            self.cmd(0, 0.1) 

        elif data.position[0] <410:
            rospy.loginfo('go')
            self.cmd(0.1, 0)

        else:
            rospy.loginfo('turn left')
            self.cmd(0, -0.1)

    def cmd(self, linear, angular):
        cmd_msg=Twist()
        cmd_msg.linear.x=linear
        cmd_msg.linear.y=0
        cmd_msg.linear.z=0
        cmd_msg.angular.x=0
        cmd_msg.angular.y=0
        cmd_msg.angular.z=angular
        self.pubs['cmd_vel'].publish(cmd_msg)
    
if __name__ == '__main__':
    rospy.init_node('pubcmd', anonymous=True)
    cls_=human_tracker()
    rospy.spin()