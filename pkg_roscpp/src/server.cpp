//reference: http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29

#include "ros/ros.h"
#include "pkg_roscpp/simple_srv.h"

bool add(pkg_roscpp::simple_srv::Request  &req,
        pkg_roscpp::simple_srv::Response &res){
  res.sum = req.a + req.b + req.c;
  ROS_INFO("request: X=%ld, Y=%ld, Z=%ld", (long int)req.a, (long int)req.b, (long int)req.c);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv){
  ros::init(argc, argv, "server_node");
  ros::NodeHandle node_obj;

  ros::ServiceServer service_obj = node_obj.advertiseService("add_ints_service", add);
  ROS_INFO("Ready to add three ints.");
  ros::spin();

  return 0;
}