/*
A simple Publisher, publishes numbers at 10hz of type std_msgs::Int32 
incrementing starting 0 to /numbers topic
*/

#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc, char **argv){
    ros::init(argc, argv, "publisher");
    ros::NodeHandle node_obj;
    ros::Publisher publisher_obj = node_obj.advertise<std_msgs::Int32>("/numbers", 10);
    ros::Rate loop_rate(10);
    
    std_msgs::Int32 msg;
    int count = 0;
    
    while (ros::ok()){
        msg.data = count;
        ROS_INFO("%d",msg.data);
        publisher_obj.publish(msg);
        
        ros::spinOnce();
        loop_rate.sleep();
        count++;
    }

    return 0;
}