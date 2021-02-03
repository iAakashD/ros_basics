#!/usr/bin/env python

import rospy
from pkg_rospy.srv import simple_srv, simple_srvResponse

def srv_handle(req):
    rospy.loginfo("request: X=%d, Y=%d, Z=%d", req.a, req.b, req.c)
    rospy.loginfo("response: sum=%d", req.a+req.b+req.c)
    return simple_srvResponse(req.a + req.b + req.c)

def main():
    rospy.init_node('server', anonymous=False)
    server = rospy.Service('add_ints_service', simple_srv, srv_handle)
    rospy.loginfo("Ready to add three ints")
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass