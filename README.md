# IRC 1410 FlexPendant Control - ABB RobotStudio

This repository contains my project assignments for the graduate-level course: BITS F441 - Robotics, under Dr B K Raut. I passed the course with the highest possible grade.
The project specifically consists of development of **inverse and direct kinematic models** as well as **dynamic models** of 3 axis articulated robotic arm. At a later stage, I was supposed to simulate IRB 1410 in ABB RobotStudio using FlexPendant IRC5 controller. 

![download](https://user-images.githubusercontent.com/47540320/114083597-d0470e00-98cc-11eb-8478-b68d7aaaeb8b.jpg)![image_327413_1](https://user-images.githubusercontent.com/47540320/114073489-f5358400-98c0-11eb-9f96-5e7777a416f2.png)

The files description is present in this readme and for further details, refer to the final reports of individual tasks. 

---

## Files description and Agenda

 1. **RRR Forward and Inverse Kinematics using Hand Calculations** - This assignment involved the calculation of DH Parameters and the Forward and Inverse Kineamatic Equations using Jacobians, The analysis was done using hand calcultion as well as in simulation. A L-RRR robot was used for analysis purpose.
![Fig](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Problem.jpg)

Have a look at the file [Scara_setup](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Scara_setup.ipynb) for the pybullet simulation file.
The hand calculations and analysis report is present [here](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Robotics_Assignment_1_Jash_Shah.pdf)

![DH-Parameters](https://www.researchgate.net/profile/Hayder-Al-Assadi/publication/271608615/figure/tbl1/AS:392071643975699@1470488572882/D-H-Parameters-of-the-IRB1410-Robot.png)



 2. **Dynamics of Robotic Arm**  - The hand report is present [here](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/2018A8PS0507P_Robotics_Assignmemt-2.pdf). The purpose of this project was to find the control torque for a RRR robotic arm when it is affected with an external force at the end-effector.

[Python Script for Automatic Calculations](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/main_script.py) and [Python script for matrix multiplication](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Robotics_assignment.py) involve **Spicy-python interface**.

### **__Newton-Euler and Lagrange Methods were used with recurrsion for finding the force, and torque vectors.__**

![download](https://user-images.githubusercontent.com/47540320/114085913-9f1c0d00-98cf-11eb-9aa5-01470f888665.jpg)


 3. **ABB RobotStudio IRB 1410 articulated arm control**

![Workspace of IRB 1410](https://user-images.githubusercontent.com/47540320/113731014-09894d80-9716-11eb-96dd-e1c877f020ca.PNG)![ABB1410](https://user-images.githubusercontent.com/47540320/113704089-527ed900-96f9-11eb-9dc2-9f124751e2d3.jpg) 

Details of this project are present in the readme file inside the directory. A short demostration gif is present below.

 4. **Saddle Point** - This was just a utility function created in MATLAB for experimenting with saddle points.

---

# Setup Instructions

The corresponding sections show the setup guide to the softwares that I have used. It also contains the setup up guide for loading my project.

## ABB RobotStudio

Download the official version of [RobotStudio](https://new.abb.com/products/robotics/robotstudio) and the operating manual from [here](https://library.e.abb.com/public/4b4d0a7f1e14fcdac1257c13004f1121/3HAC032104-en.pdf).

The software contains a premium version which is paid, but they also provide a trial version for 30 days. Download the trial version, extract the files and initiate the installation process from setup.exe.

Once everything is setup, clone my repository, and open the [**Assignment_letter.rssln**](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/ABB%20RobotStudio%20IRB%201410%20articulated%20arm%20control/Assignment_Letter.rar) file. 

Make sure you install the **RobotWare 6.0 IRC5** controller Add-on. This will allow you to access the virtual Flexpendant controller. 

Once everything is setup, follow the steps in my [video demonstration](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Assignment_Output.mp4).

![RobotController](https://user-images.githubusercontent.com/47540320/113730350-7223fa80-9715-11eb-9e09-782bf126a44a.PNG)


## Anaconda-Pybullet Setup

To install Anaconda follow the instructions in the following webpage:  
https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart

Create a conda environment for the PyBullet tutorial:  
```
$ conda create --name pyb_env  
```
Switch to the newly create environment (you will notice the name of the environment on the command line in the extreme left):  
```
$ conda activate pyb_env  
```

Once in the desired environment install the following packages:  
```
$ conda install nb_conda_kernels  
```

Install PyBullet (while in the environment):  
```
$ pip install pybullet  
```

Install Matplotlib (while in the environment):
```
$ conda install matplotlib
```



To check the installation launch:  
```
$ python  
```

Inside the python environment import the pybullet and matplotlib libraries:  
```
>> import pybullet
>> import matplotlib
```
If this command executes without any error then the installation is successful.  


Check the Jupyter notebook by running the following command in the bash shell:  
```
$ jupyter notebook  
```
This command will provide a URL. Run the URL in a browser (Firefox). If a web page opens up, then the Jupyter software is successfully installed.  

---

## References

  * RobotStudio Tutorials by [Hogskolani Skovde University](https://his.instructure.com/courses/3328/pages/robotstudio-tutorial-video-library)
  * ABB Tutorial by [CHETAN JALENDRA](https://drive.google.com/file/d/1mdPkSNv2JhjNpQBhUM0tqa1tpV0jWVSs/view?usp=sharing)
  * Official ABB RobotStudio [Tutorials](https://new.abb.com/products/robotics/robotstudio/tutorials)
  * Complete Tutorial of RobotStudio | [Youtube](https://www.youtube.com/watch?v=9kp-YR6hoGk&list=PL7vknECtgBIyxmhZDBx3xj0AGNcyxt93b)
  * British Columbia Institute of Technology Mechatronics and Robotics [Tutorials for ABB RobotStudio](https://www.youtube.com/watch?v=9kp-YR6hoGk)
  * RobotStudio tutorial for beginners by [viktor007r](https://www.youtube.com/watch?v=kQax9-TvrHE)
  * [ABB RobotStudio Forum](https://forums.robotstudio.com/discussion/74/differences-movejoint-moveline) | differences - MoveJoint / MoveLine

