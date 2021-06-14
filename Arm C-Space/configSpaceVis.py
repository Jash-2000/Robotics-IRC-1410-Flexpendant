import numpy as np
import matplotlib as plt
import cv2
import math


def forwardKinematics(a1, a2, q1, q2):
    return [a1*np.cos(math.pi/180*q1)+a2*np.cos(math.pi/180*(q1+q2)), a1*np.sin(math.pi/180*q1)+a2*np.sin(math.pi/180*(q1+q2))]


def inverseKinematics(x, y, a1, a2):
    q2 = np.arccos((x**2+y**2-a1**2-a2**2)/(2*a1*a2))
    q1 = np.arctan(y/x)-np.arctan(a2*np.sin(q2)/(a1+a2*np.cos(q2)))
    return (int(np.degrees(q1)), int(np.degrees(q2)))


# We are sure the given obstacles are rectangular and are defined as specified
def collisionCheck(obstacle, pos):
    if pos[0] > obstacle[0][0] and pos[0] < obstacle[0][1] and pos[1] > obstacle[1][0] and pos[1] < obstacle[1][1]:
        return 1
    return 0


a1 = 5
a2 = 6

obstacle1 = [[3, 8], [-5, -3]]  # define obstacles as [[x1, x2], [y1, y2]]
obstacle2 = [[-5, -2], [5, 8]]

collisions_x = []
collisions_y = []
lengthToCheck = 0

img = np.zeros((360, 360, 3), np.float64)

for i in range(0, 361):
    q1 = i
    for j in range(0, 361):
        q2 = j
        for lengthToCheck in np.arange(13, 0, -0.2):

            if lengthToCheck < a2:
                pos = forwardKinematics(a1, a2-lengthToCheck, q1, q2)
                collides = collisionCheck(obstacle1, pos)
                if collides:
                    cv2.circle(img, (i, j), 1, (0, 255, 0))
                collides = collisionCheck(obstacle2, pos)
                if collides:
                    cv2.circle(img, (i, j), 1, (0, 255, 0))

            if lengthToCheck > a2:
                pos = forwardKinematics(a2+a1-lengthToCheck, 0, q1, q2)
                collides = collisionCheck(obstacle1, pos)
                if collides:
                    cv2.circle(img, (i, j), 1, (0, 255, 0))
                collides = collisionCheck(obstacle2, pos)
                if collides:
                    cv2.circle(img, (i, j), 1, (0, 255, 0))

startingPoint = inverseKinematics(3, -6, a1, a2)
goalPoint = inverseKinematics(-1, 7, a1, a2)

cv2.circle(img, (360+startingPoint[0], startingPoint[1]), 5, (0, 0, 255))
cv2.circle(img, (goalPoint[0]+180, goalPoint[1]), 5, (0, 255, 0))

cv2.line(img, (180, 0), (180, 360), (255, 0, 0), 1)
cv2.line(img, (0, 180), (360, 180), (255, 0, 0), 1)

cv2.imshow('Configuration Space Graph', img)

cv2.waitKey(0)
