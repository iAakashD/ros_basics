#!/usr/bin/env python

import rospy
from pkg_rospy.msg import simple_msg

def main():
    rospy.init_node('msg_publisher_py', anonymous=False)
    pub = rospy.Publisher('/topic_publisher_msg', simple_msg, queue_size=10)
    rate = rospy.Rate(10)
    msg = simple_msg()
    
    while not rospy.is_shutdown():
        msg.boolean = False
        msg.num = 100
        msg.unsigned_num = 50000
        msg.float_num = 10.0
        msg.double_num = 50.0
        msg.str = "Hello"
        pub.publish(msg)
        rospy.loginfo("Custom message sent")
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass