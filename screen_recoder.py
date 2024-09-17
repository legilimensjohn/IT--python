import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)

code= cv2.VideoWriter_fourcc(*"XVID")

fileName = "Recording.avi"

fps = 60.0

out = cv2.VideoWriter(fileName, code, fps, resolution)

cv2.nameWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 500, 280)
