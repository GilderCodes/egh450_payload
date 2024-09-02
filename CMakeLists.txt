cmake_minimum_required(VERSION 3.0.2)
project(egh450_payload)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
)

## Declare a catkin package
catkin_package()

## Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Install Python scripts
catkin_install_python(PROGRAMS
  scripts/drop_payload.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
