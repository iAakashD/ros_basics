cmake_minimum_required(VERSION 3.0.2)
project(pkg_roscpp)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  message_generation
)

add_message_files(FILES
  simple_msg.msg
)

add_service_files(FILES
  simple_srv.srv
)

generate_messages(DEPENDENCIES
  std_msgs
)

catkin_package(CATKIN_DEPENDS
  std_msgs
  message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(publisher src/publisher.cpp)
target_link_libraries(publisher ${catkin_LIBRARIES})

add_executable(subscriber src/subscriber.cpp)
target_link_libraries(subscriber ${catkin_LIBRARIES})

add_executable(publisher_msg src/publisher_msg.cpp)
add_dependencies(publisher_msg pkg_roscpp_generate_messages_cpp)
#add the above line to compile .msg file and create .h from it before compiling publisher_msg.cpp node
target_link_libraries(publisher_msg ${catkin_LIBRARIES})

add_executable(subscriber_msg src/subscriber_msg.cpp)
add_dependencies(subscriber_msg pkg_roscpp_generate_messages_cpp)
target_link_libraries(subscriber_msg ${catkin_LIBRARIES})

add_executable(client src/client.cpp)
add_dependencies(client pkg_roscpp_generate_messages_cpp)
target_link_libraries(client ${catkin_LIBRARIES})

add_executable(server src/server.cpp)
add_dependencies(server pkg_roscpp_generate_messages_cpp)
target_link_libraries(server ${catkin_LIBRARIES})
