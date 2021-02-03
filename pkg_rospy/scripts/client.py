#!/usr/bin/env python

#for some strange reason rospy.loginfo is not working, not even throwing an error ..
# .. in client script, used native python print instead

import sys
import rospy
from pkg_rospy.srv import simple_srv

def client(x, y, z):
    rospy.wait_for_service('add_ints_service')
    add_ints = rospy.ServiceProxy('add_ints_service', simple_srv)
    try:
        add_ints = rospy.ServiceProxy('add_ints_service', simple_srv)
        res = add_ints(x, y, z)
        return res.sum
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        X = int(sys.argv[1])
        Y = int(sys.argv[2])
        Z = int(sys.argv[3])
        
        print("Requesting from server")
        print("Got response: %d" %client(X, Y, Z))
    else:
        print("Enter in the form: rosrun.. X Y Z")
        sys.exit(1)