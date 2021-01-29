/*
Subscriber, reads numbers in /numbers topic and shows it on console via ROS_INFO
*/

#include "ros/ros.h"
#include "std_msgs/Int32.h"

void numbers_callback(const std_msgs::Int32::ConstPtr& msg){
    ROS_INFO("number is: [%d]", msg->data);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "subscriber");
    ros::NodeHandle node_obj;
    ros::Subscriber subscriber_obj = node_obj.subscribe("/numbers", 10, numbers_callback);

    ros::spin();
    return 0;
}