#!/usr/bin/env python

import rospy
from pkg_rospy.msg import simple_msg

def callback_fun(data):
    rospy.loginfo("I heard [%d]", data.num)

def main():
    rospy.init_node('msg_subscriber_py', anonymous=False)
    sub = rospy.Subscriber('/topic_publisher_msg', simple_msg, callback_fun)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass