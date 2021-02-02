#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback_fun(data):
    rospy.loginfo("I heard [%d]", data.data)

def main():
    rospy.init_node('subscriber', anonymous=False)
    sub = rospy.Subscriber('/numbers', Int32, callback_fun)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass