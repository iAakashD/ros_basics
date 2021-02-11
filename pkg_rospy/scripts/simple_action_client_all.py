#! /usr/bin/env python

# Sends goal and does its work, done_cb callback function is invoked whenever a 
# msg on /count_numbers/result is received, feedback function is incoked 
# whenever a msg on /count_numbers/feedback is received

# reference: https://docs.ros.org/en/melodic/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html

import rospy
import actionlib
from pkg_rospy.msg import CountNumbersAction, CountNumbersGoal

class CountNumbersClient():
    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/count_numbers', CountNumbersAction)
        self._ac.wait_for_server()
        rospy.loginfo("connected to actionserver")

    def send_goal(self):
        goal = CountNumbersGoal()
        goal.count_upto = 10
        goal.wait_time = 1.0
        self._ac.send_goal(goal, done_cb = self.done_cb, feedback_cb=self.feedback_cb)
        rospy.loginfo("Goal has been sent")

        #rospy.sleep(1)     #uncomment to cancel goal while execution
        #self._ac.cancel_goal()
    
    def done_cb(self, status, result):
        rospy.loginfo("status is: " + str(status))
        rospy.loginfo("result is: " + str(result))  #3 means success, 4 means aborted, reference: http://docs.ros.org/en/kinetic/api/actionlib_msgs/html/msg/GoalStatus.html
        rospy.logwarn("Shutting down node")
        rospy.signal_shutdown("Done Executing")

    def feedback_cb(self, feedback):
        rospy.loginfo("feedback is: " + str(feedback))

def main():
    rospy.init_node("count_numbers_client")
    Client = CountNumbersClient()
    Client.send_goal()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass