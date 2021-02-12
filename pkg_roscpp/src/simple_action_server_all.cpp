// reference: https://docs.ros.org/en/melodic/api/actionlib/html/classactionlib_1_1SimpleActionServer.html

#include "ros/ros.h"
#include "actionlib/server/simple_action_server.h"
#include "pkg_roscpp/CountNumbersAction.h"

class ActionServer{
protected:
    ros::NodeHandle nh_;
    actionlib::SimpleActionServer<pkg_roscpp::CountNumbersAction> as_;

    pkg_roscpp::CountNumbersFeedback feedback_;
    pkg_roscpp::CountNumbersResult result_;

public:
    ActionServer(std::string name) : 
            as_(nh_, name, boost::bind(&ActionServer::executeCB, this, _1), false)
    {
        as_.start();
        ROS_INFO("Action Server started");
    }

    ~ActionServer(void){}

    void executeCB(const pkg_roscpp::CountNumbersGoalConstPtr &goal){
        int32_t count = 0;
        int32_t count_upto = goal->count_upto;
        float wait_time = goal->wait_time;
        ROS_INFO("Goal received, count_upto: [%d], wait_time: [%f]", count_upto, wait_time);

        ros::Rate rate(1.0/wait_time);

        bool some_error_occoured = false;
        bool preempt_reuested = false;
        pkg_roscpp::CountNumbersFeedback feedback_;

        while (!ros::isShuttingDown() && count<count_upto){
            if (some_error_occoured)
                break;
            if (as_.isPreemptRequested()){
                preempt_reuested = true;
                break;
            }
            
            count++;
            feedback_.current_count = count;
            as_.publishFeedback(feedback_);

            rate.sleep();
        }
        result_.final_count = count;

        if (some_error_occoured){
            as_.setAborted(result_);
            ROS_WARN("Goal aborted");
        }
        else if(preempt_reuested){
            as_.setPreempted(result_);
            ROS_WARN("Goal preempted");
        }
        else{
            as_.setSucceeded(result_);
            ROS_INFO("Goal completed succesfully");
        }
    }
};

int main(int argc, char **argv){
    ros::init(argc, argv, "simple_action_server_all");
    ActionServer Server("count_numbers");

    ros::spin();

    return 0;
}