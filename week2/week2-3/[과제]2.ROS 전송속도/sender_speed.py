#! /usr/bin/env python

import rospy
from std_msgs.msg import String

name = "sender"
pub_topic = "long_string"

rospy.init_node(name, anonymous=True)
pub = rospy.Publisher(pub_topic, String, queue_size=1)

hello_str = String()
rate = rospy.Rate(1)

pub_size = 1000000
#pub_size = 50000000
#pub_size = 100000000
#pub_size = 200000000
#pub_size = 500000000

my_string = ""

for i in range(pub_size):
	my_string += "#"

while not rospy.is_shutdown():
	hello_str.data = my_string + ":" + str(rospy.get_time())
	pub.publish(hello_str)
	rate.sleep()
