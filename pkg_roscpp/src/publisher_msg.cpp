#include "ros/ros.h"
#include "pkg_roscpp/simple_msg.h"

int main(int argc, char **argv){
    ros::init(argc, argv, "publisher");
    ros::NodeHandle node_obj;
    ros::Publisher publisher_obj = node_obj.advertise<pkg_roscpp::simple_msg>("/topic_publisher_msg", 10);
    ros::Rate loop_rate(10);
    
    pkg_roscpp::simple_msg msg;
    uint8_t bool_val = true;
    int32_t num_val = 0;  //int32 in ros msg corresponds to int32_t of c++
    uint32_t unsigned_num_val = 10;
    float float_val = 0.0f;
    double double_val = 0.0;
    std::string text = "Hello World";   //string corresponds to std::string (c++ style string)

    while (ros::ok()){
        msg.boolean = bool_val;
        msg.num = num_val;
        msg.unsigned_num = unsigned_num_val;
        msg.float_num = float_val;
        msg.double_num = double_val;
        msg.str = text;

        ROS_INFO("%d",msg.num);
        ROS_INFO("%s", (msg.str).c_str());  //convert c++ string to c string for printing
        publisher_obj.publish(msg);
        
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}