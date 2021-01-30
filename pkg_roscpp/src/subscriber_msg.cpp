#include "ros/ros.h"
#include "pkg_roscpp/simple_msg.h"

void numbers_callback(const pkg_roscpp::simple_msg::ConstPtr& msg){
    ROS_INFO("number is: [%d]", msg->num);
}

int main(int argc, char **argv){
    ros::init(argc, argv, "subscriber");
    ros::NodeHandle node_obj;
    ros::Subscriber subscriber_obj = node_obj.subscribe("/topic_publisher_msg", 10, numbers_callback);

    ros::spin();
    return 0;
}