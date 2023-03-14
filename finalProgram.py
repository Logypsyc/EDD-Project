# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys
import pygame


pygame.mixer.init()

def audioLoader(instruction):
	switcher = {
		"welcome": "/home/pi/Documents/audioFiles/welcome.mp3",
		"turnLeftAndForward": "/home/pi/Documents/audioFiles/turnLeftAndForward.mp3",
		"turnRightAndForward": "/home/pi/Documents/audioFiles/turnRightAndForward.mp3",
		"keepForward": "/home/pi/Documents/audioFiles/keepForward.mp3",
		"arrived": "/home/pi/Documents/audioFiles/arrived.mp3",
	}
	return switcher.get(instruction)

# load the ArUCo dictionary and grab the ArUCo parameters
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters_create()

# initialize the video stream and allow the camera sensor to warm up
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to have a maximum width of 1000 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=1000)
	# detect ArUco markers in the input frame
	(corners, ids, rejected) = cv2.aruco.detectMarkers(frame, arucoDict, parameters=arucoParams)

	# verify *at least* one ArUco marker was detected
	if len(corners) > 0:
		# flatten the ArUco IDs list
		ids = ids.flatten()
		# loop over the detected ArUCo corners
		for (markerCorner, markerID) in zip(corners, ids):
			# extract the marker corners (which are always returned in top-left, top-right, bottom-right, and bottom-left order)
			corners = markerCorner.reshape((4, 2))
			(topLeft, topRight, bottomRight, bottomLeft) = corners
			# convert each of the (x, y)-coordinate pairs to integers
			topRight = (int(topRight[0]), int(topRight[1]))
			bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
			bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
			topLeft = (int(topLeft[0]), int(topLeft[1]))

			# draw the bounding box of the ArUCo detection
			cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)
			# compute and draw the center (x, y)-coordinates of the ArUco marker
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
			# draw the ArUco marker ID on the frame
			cv2.putText(frame, str(markerID), (topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

			if markerID == 0:
				instruction = "welcome"
				pygame.mixer.music.load(audioLoader(instruction))
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue

			if markerID == 1:
				instruction = "turnLeftAndForward"
				pygame.mixer.music.load(audioLoader(instruction))
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue

			if markerID == 2:
				instruction = "turnRightAndForward"
				pygame.mixer.music.load(audioLoader(instruction))
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue

			if markerID == 3:
				instruction = "keepForward"
				pygame.mixer.music.load(audioLoader(instruction))
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue

			if markerID == 4:
				instruction = "arrived"
				pygame.mixer.music.load(audioLoader(instruction))
				pygame.mixer.music.play()
				while pygame.mixer.music.get_busy() == True:
					continue


	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
