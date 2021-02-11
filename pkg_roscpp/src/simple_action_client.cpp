#include "ros/ros.h"
#include "actionlib/client/simple_action_client.h"
#include "pkg_roscpp/CountNumbersAction.h"

class ActionClient{
protected:
    ros::NodeHandle nh_;
    actionlib::SimpleActionClient<pkg_roscpp::CountNumbersAction> ac_;

public:
    ActionClient() : 
        ac_("count_numbers", true)
    {
        ROS_INFO("waiting for server to start");
        ac_.waitForServer();    
    }

    ~ActionClient(void){}

    void send_goal(){
        ROS_INFO("connected to server");
        pkg_roscpp::CountNumbersGoal goal;
        goal.count_upto = 10;
        goal.wait_time = 1.0;
        ac_.sendGoal(goal, 
                boost::bind(&ActionClient::done_CB, this, _1, _2)); //_1 _2 -> number of arguments in done_CB()
        ROS_INFO("goal sent");
    }

    void done_CB(const actionlib::SimpleClientGoalState &state, 
            const pkg_roscpp::CountNumbersResultConstPtr &result)
    {
        //ROS_INFO("Finished in state: %s", (state).toString.c_str());
        ROS_INFO("Result: [%d]", (int)result->final_count);
    }
};

int main(int argc, char **argv){
    ros::init(argc, argv, "simple_action_client");
    ActionClient Client;
    Client.send_goal();
    ros::spin();
    return 0;
}