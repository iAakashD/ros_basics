#! /usr/bin/env python

# Sends goal and waits for result, similar to ordinary client-server setup

import rospy
import actionlib
from pkg_rospy.msg import CountNumbersAction, CountNumbersGoal

class CountNumbersClient():
    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/count_numbers', CountNumbersAction)
        self._ac.wait_for_server()
        rospy.loginfo("connected to actionserver")

    def send_goal_get_result(self):
        goal = CountNumbersGoal()
        goal.count_upto = 10
        goal.wait_time = 1.0
        self._ac.send_goal(goal)
        rospy.loginfo("Goal has been sent")
        success = self._ac.wait_for_result(rospy.Duration(12.0))
        if not success:
            rospy.logwarn("Timeout")
        rospy.loginfo(self._ac.get_result())

def main():
    rospy.init_node("count_numbers_client")
    Client = CountNumbersClient()
    Client.send_goal_get_result()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass