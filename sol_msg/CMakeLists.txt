cmake_minimum_required(VERSION 3.0.2)
project(sol_msg)

find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs message_generation)

add_message_files(
  DIRECTORY msg
  FILES
  track.msg
)



 generate_messages(
   DEPENDENCIES
   std_msgs
)

catkin_package(
  CATKIN_DEPENDS 
  message_runtime std_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

