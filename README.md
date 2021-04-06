# Robotics-BITS-Pilani
This repository contains my project assignments for the graduate-level course: BITS F441 - Robotics, under Dr B K Raut. I passed the course with the highest possible grade.

![RobotController](https://user-images.githubusercontent.com/47540320/113730350-7223fa80-9715-11eb-9e09-782bf126a44a.PNG)


## Tech Stack


## Files description and Agenda

 * RRR Forward and Inverse Kinematics using Hand Calculations
 * Dynamics of Robotic Arm
 * ABB RobotStudio IRB 1410 articulated arm control
![ABB1410](https://user-images.githubusercontent.com/47540320/113704089-527ed900-96f9-11eb-9dc2-9f124751e2d3.jpg) ![](https://www.researchgate.net/profile/Hayder-Al-Assadi/publication/271608615/figure/tbl1/AS:392071643975699@1470488572882/D-H-Parameters-of-the-IRB1410-Robot.png)


---

# Setup Instructions

## ABB RobotStudio


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
  * 

