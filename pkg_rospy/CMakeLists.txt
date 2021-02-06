cmake_minimum_required(VERSION 3.0.2)
project(pkg_rospy)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  actionlib
  actionlib_msgs
)

add_message_files(FILES
  simple_msg.msg
)

add_service_files(FILES
  simple_srv.srv
)

add_action_files(FILES
  CountNumbers.action
)

generate_messages(DEPENDENCIES
  std_msgs
  actionlib_msgs
)

catkin_package(CATKIN_DEPENDS
  std_msgs
  message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/publisher.py
  scripts/subscriber.py
  scripts/publisher_msg.py
  scripts/subscriber_msg.py
  scripts/simple_action_client.py
  scripts/simple_action_server.py
  
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)