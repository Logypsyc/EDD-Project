from apriltag import apriltag
import cv2
import numpy as np
import pygame
from picamera2 import Picamera2

cam = Picamera2()
cam.configure(cam.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
cam.start()
cv2.namedWindow("camera POV")
pygame.mixer.init()

while True:
        frame = cam.capture_array()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detector = apriltag("tagStandard41h12")
        results = detector.detect(gray)

        for r in results:
                print("kock")
                pygame.mixer.music.load("/home/pi/Documents/vineBoomSoundEffect.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                        continue

        cv2.imshow("camera POV", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break

cam.release()

cv2.destroyAllWindows()
