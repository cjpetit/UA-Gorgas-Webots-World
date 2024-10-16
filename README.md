# UA-Gorgas-Webots-World

To launch the simulation world using ros2_webots on linux (or wsl), cd into the directory and run the following:
  1. source /opt/ros/humble/setup.bash
  2. export WEBOTS_HOME=/mnt/c/Program\ Files/Webots
  3. colcon build
  4. source install/setp.bash
  5. ros2 launch project_p1 p1_launch.py
