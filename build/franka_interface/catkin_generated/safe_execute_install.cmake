execute_process(COMMAND "/home/seungbeom/franka_ws/build/franka_interface/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/seungbeom/franka_ws/build/franka_interface/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
