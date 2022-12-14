# Hongdo robot : Ansan Mascot Promotional Robot
main project | https://github.com/Hanyang-WAB/hongdo_system <br><br>

# hongdo_ros_soft
![hong_do_1](https://user-images.githubusercontent.com/98142691/192149706-c6497f09-81c8-448e-b132-7e2f2a023c04.gif)
![hong_do_2](https://user-images.githubusercontent.com/98142691/192149740-f85e851a-8d84-4f00-83b9-605ca63cdc51.gif)

## Description
- ### Reference
  We designed the robot by referring to the following site. The robot recognizes obstacle based on the Yolov5 and can track people.  
  * **Yolov5_StrongSORT_OSNet** | https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet#introduction <br><br>  
    
- ### Introduction
  Hongdo_ros_soft contains the content that the robot recognizes and follows a person.
    * **Human track**: Based on the YoloV5, the robot tracking people and obtains the size and coordinates for nearest person
    * **Import ROS**: This package sends the output that size, number, coordinate of recogniged person.
    * **Human following**: Depending on the location and distance from the person, the robot approaches the person and stops at a certain distance
 

## Installation
We used a Jetson nano with Jetpack 4.6.1 and ROS melodic installed.

- ### Install opencv 4.5.4
  The installation of opencv is required to run this package.
    ```
    $ wget https://github.com/Qengineering/Install-OpenCV-Jetson-Nano/raw/main/OpenCV-4-5-4.sh
    $ sudo chmod 755 ./OpenCV-4-5-4.sh
    $ ./OpenCV-4-5-4.sh
    ```
  
- ### Install PyTorch 1.8 + torchvision v0.9.0
  The installation of Pytorch and torchvision is required to run this package.
  
    ```
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
    ```
  
- ### Requirement
  Make sure that you fulfill all the requirements: Python 3.6.9 or later with all requirements.txt dependencies installed, including torch>=1.7. To install, run:
  
    ```
    $ cd track/src
    $ pip install -r requirements.txt
    ```
    
## Getting Started
- ### Build
  To run this package, clone the package and build it.
  
    ```
    $ cd ~/catkin_ws/src
    $ git clone https://github.com/coldbell8918/Hongdo_soft.git
    $ cd ~/catkin_Ws
    $ catkin_make
    ```
  
- ### Run
  Run through the following command
  
    ```
    $ roslaunch track hongdo_ros_vision.launch
    ```

