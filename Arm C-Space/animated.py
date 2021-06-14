import cv2
import numpy as np
import math
import matplotlib.pyplot as plt


def forwardKinematics(a1, a2, q1, q2, origin):
    return (origin[0] + np.int(a1 * np.cos(math.pi / 180 * q1) + a2 * np.cos(math.pi / 180 * (q1 + q2))),
            origin[1] + np.int(a1 * np.sin(math.pi / 180 * q1) + a2 * np.sin(math.pi / 180 * (q1 + q2))))


def inverseKinematics(x, y, a1, a2):
    q2 = np.arccos((x ** 2 + y ** 2 - a1 ** 2 - a2 ** 2) / (2 * a1 * a2))
    q1 = np.arctan(y / x) - np.arctan(a2 * np.sin(q2) / (a1 + a2 * np.cos(q2)))
    return (int(np.degrees(q1)), int(np.degrees(q2)))


img = np.zeros((400, 400, 3), np.float64)

origin = (200, 200)
cv2.circle(img, origin, 5, (255, 0, 0), -1)
cv2.circle(img, (-1*20+200, -7*20+250), 5, (0, 255, 0))
cv2.circle(img, (3*20+200, 6*20+200), 5, (0, 0, 255))

cv2.line(img, (200, 0), (200, 400), (255, 0, 0), 1)
cv2.line(img, (0, 200), (400, 200), (255, 0, 0), 1)
cv2.imshow('2Link Robot Configuration', img)
cv2.rectangle(img, (-5*20+200, -8*20+250),
              (-2*20+200, -5*20+200), (33, 102, 242), -1)
cv2.rectangle(img, (3*20+200, 3*20+200),
              (8*20+200, 5*20+200), (33, 102, 242), -1)

arm1 = 100  # length of the arm hinged to the ground
arm2 = 120  # length of the arm hinged to arm1

theta = 0
configs = np.array([[238, 105],  # aarbitrary path
                    [225, 113],
                    [214, 118],
                    [202, 123],
                    [190, 127],
                    [177, 131],
                    [161, 134],
                    [145, 139],
                    [129, 140],
                    [114, 141],
                    [98, 143],
                    [83, 144],
                    [70, 145],
                    [56, 144],
                    [49, 139],
                    [39, 132],
                    [33, 120],
                    [38, 108],
                    [42, 100]])
i = len(configs)-1
i = 0
while i < len(configs)-1:
    tempImg = img.copy()
    endingPoint1 = (np.int(arm1*np.cos(np.pi*configs[i][0]/180)+origin[0]), np.int(
        arm1*np.sin(-np.pi*configs[i][0]/180)+origin[1]))
    endingPoint2 = forwardKinematics(
        arm1, arm2, -configs[i][0], -configs[i][1], origin)

    print(endingPoint2)
    cv2.line(tempImg, origin, endingPoint1, (0, 255, 0), 9)
    cv2.line(tempImg, endingPoint1, endingPoint2, (0, 255, 0), 9)
    cv2.circle(tempImg, origin, 8, (255, 0, 0), -1)
    cv2.circle(tempImg, endingPoint1, 8, (255, 0, 0), -1)
    i = i + 1
    cv2.waitKey(200)
    cv2.imshow('2Link Robot Configuration', tempImg)

cv2.waitKey(0)
cv2.destroyWindow()
