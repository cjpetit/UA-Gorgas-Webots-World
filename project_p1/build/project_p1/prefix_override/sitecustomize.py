import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/colepetit/ros2_ws/src/project_p1/install/project_p1'
