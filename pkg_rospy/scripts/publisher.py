#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def main():
    rospy.init_node('publisher', anonymous=False)
    pub = rospy.Publisher('/numbers', Int32, queue_size=10)
    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        rospy.loginfo("Sent [%d]", count)
        pub.publish(count)
        rate.sleep()
        count = count+1

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
