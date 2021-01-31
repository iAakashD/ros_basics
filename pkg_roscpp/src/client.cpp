#include "ros/ros.h"
#include "pkg_roscpp/simple_srv.h"
#include <cstdlib>

int main(int argc, char **argv){
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 4)
  {
    ROS_INFO("usage: add_two_ints_client X Y Z");
    return 1;
  }

  ros::NodeHandle node_obj;
  ros::ServiceClient client_obj = node_obj.serviceClient<pkg_roscpp::simple_srv>("add_ints_service");
  pkg_roscpp::simple_srv srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  srv.request.c = atoll(argv[3]);
  if (client_obj.call(srv)){
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else{
    ROS_ERROR("Failed to call service add_three_ints");
    return 1;
  }

  return 0;
}