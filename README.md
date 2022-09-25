# Hongdo robot : Ansan Mascot Promotional Robot
main project | https://github.com/Hanyang-WAB/hongdo_system <br><br>

# hongdo_ros_soft
## Description
write description

## installation
We used a Jetson nano with Jetpack 4.6.1 and ROS melodic installed.

- ### install opencv 4.5.4
  The installation of opencv is required to run this package.
  
    '$ wget https://github.com/Qengineering/Install-OpenCV-Jetson-Nano/raw/main/OpenCV-4-5-4.sh'
    $ sudo chmod 755 ./OpenCV-4-5-4.sh
    $ ./OpenCV-4-5-4.sh
  
  
- ### install PyTorch 1.8 + torchvision v0.9.0
  The installation of Pytorch and torchvision is required to run this package.
  
  '''
    $ wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl -O torch-1.8.0-cp36-cp36m-linux_aarch64.whl
    $ sudo apt-get install python3-pip libopenblas-base libopenmpi-dev
    $ pip3 install Cython
    $ pip3 install numpy torch-1.8.0-cp36-cp36m-linux_aarch64.whl
    $ sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
    $ git clone --branch v0.9.0 https://github.com/pytorch/vision torchvision
    $ cd torchvision
    $ export BUILD_VERSION=0.9.0
    $ python3 setup.py install --user
    $ cd ../  
  '''
  
- ### requirement
  Make sure that you fulfill all the requirements: Python 3.6.9 or later with all requirements.txt dependencies installed, including torch>=1.7. To install, run:
  
  '''
    $ cd track/src
    $ pip install -r requirements.txt
  '''
    
## Getting Started
- ### build
  To run this package, clone the package and build it.
  
  '''
    $ cd ~/catkin_ws/src
    $ git clone https://github.com/coldbell8918/Hongdo_soft.git
    $ cd ~/catkin_Ws
    $ catkin_make
  '''
  
- ### run
  Run through the following command
  
  '''
    $ roslaunch track hongdo_ros_vision.launch
  '''

