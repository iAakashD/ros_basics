#! /usr/bin/env python

# Counts until count_upto with wait_time between each count, sends feedback after 
# each count and sends the result on completion

# reference: https://docs.ros.org/en/melodic/api/actionlib/html/classactionlib_1_1simple__action__server_1_1SimpleActionServer.html

import rospy
import actionlib
from pkg_rospy.msg import CountNumbersAction, CountNumbersGoal, \
        CountNumbersResult, CountNumbersFeedback

class CountNumbersServer:
    def __init__(self):
        self._as = actionlib.SimpleActionServer('/count_numbers', CountNumbersAction, \
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

        feedback = CountNumbersFeedback()
        some_error_occoured = False
        preempt_reuested = False
        while (not rospy.is_shutdown()) and (self._counter < count_upto):
            if some_error_occoured:     #counting has failed due to some error
                break
            if self._as.is_preempt_requested():
                preempt_reuested = True
                break

            self._counter += 1

            feedback.current_count = self._counter
            self._as.publish_feedback(feedback)
            
            rate.sleep()
        
        result = CountNumbersResult()
        result.final_count = self._counter
        
        if some_error_occoured:
            self._as.set_aborted(result)
            rospy.logwarn("Goal aborted")
        elif preempt_reuested:
            self._as.set_preempted(result)
            rospy.logwarn("Goal Preempted")
        else:
            self._as.set_succeeded(result)
            rospy.loginfo("Goal completed succesfully")

def main():
    rospy.init_node("count_numbers_server")
    Server = CountNumbersServer()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass