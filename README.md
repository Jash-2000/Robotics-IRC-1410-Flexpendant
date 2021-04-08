# Robotics - BITS F441
This repository contains my project assignments for the graduate-level course: BITS F441 - Robotics, under Dr B K Raut. I passed the course with the highest possible grade.
The project specifically consists of development of **inverse and direct kinematic models** as well as **dynamic models** of 3 axis articulated robotic arm.

---

## Files description and Agenda

 1. **RRR Forward and Inverse Kinematics using Hand Calculations** - This assignment involved the calculation of DH Parameters and the Forward and Inverse Kineamatic Equations using Jacobians, The analysis was done using hand calcultion as well as in simulation. A L-RRR robot was used for analysis purpose.
![Fig](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Problem.jpg)

Have a look at the file [Scara_setup](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Scara_setup.ipynb) for the pybullet simulation file.
The hand calculations and analysis report is present [here](https://github.com/Jash-2000/Robotics-IRC-1410-Flexpendant/blob/master/Robotics_Assignment_1_Jash_Shah.pdf)

![DH-Parameters](https://www.researchgate.net/profile/Hayder-Al-Assadi/publication/271608615/figure/tbl1/AS:392071643975699@1470488572882/D-H-Parameters-of-the-IRB1410-Robot.png)



 2. **Dynamics of Robotic Arm**  - 


---

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
