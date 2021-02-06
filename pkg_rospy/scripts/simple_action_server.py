#! /usr/bin/env python

#Counts until count_upto with wait_time between each count and sends the result on completion

import rospy
import actionlib
from pkg_rospy.msg import CountNumbersAction, CountNumbersGoal, CountNumbersResult

class CountNumbersServer:
    def __init__(self):
        self._as = actionlib.SimpleActionServer('/count_numbers', CountNumbersAction, 
                execute_cb = self.on_goal, auto_start=False)
        self._as.start()
        rospy.loginfo("count numbers server started")

        self._counter = 0
    
    def on_goal(self, goal):
        rospy.loginfo("Goal has be en received")
        rospy.loginfo(goal)
        count_upto = goal.count_upto
        wait_time = goal.wait_time

        self._counter = 0
        rate = rospy.Rate(1.0/wait_time)

        while self._counter < count_upto:
            self._counter += 1
            rate.sleep()
        
        result = CountNumbersResult()
        result.final_count = self._counter
        self._as.set_succeeded(result)
        rospy.loginfo("result has been sent")

def main():
    rospy.init_node("count_numbers_server")
    Server = CountNumbersServer()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass