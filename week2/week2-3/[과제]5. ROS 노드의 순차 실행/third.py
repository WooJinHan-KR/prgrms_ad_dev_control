#! /usr/bin/env python

import rospy
from std_msgs.msg import String

name = "third"
pub_topic = "msg_to_receiver"
sub_topic = "start_ctl"

OK = None

def ctl_callback(data):
	global OK
	OK = str(data.data)

rospy.init_node(name)
rospy.Subscriber(sub_topic, String, ctl_callback)
