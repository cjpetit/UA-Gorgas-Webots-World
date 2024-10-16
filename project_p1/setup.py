from setuptools import setup
from glob import glob

package_name = 'project_p1'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/p1_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/part1.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/turtlebot_webots.urdf']))
data_files.append(('share/' + package_name + '/protos', glob('protos/*')))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user.name@mail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['webots_ros2_homework1_python = project_p1.webots_ros2_homework1_python:main',]
    },
)
