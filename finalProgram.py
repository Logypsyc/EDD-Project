import apriltag
import numpy
import cv2

camera_matrix = [2.06793814e+03, 0.0, 1.04217885e+03, 0.0, 2.06355504e+03, 5.59019151e+02, 0.0, 0.0, 1.0]

cam = cv2.VideoCapture(0)
cv2.namedWindow("camera POV")

while True:
	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	detector = Detector(families='tag16h5', nthreads = 1, quad_decimate = 1.0, quad_sigma = 0.0, refine_edges = 1, decode_sharpening = 0.25, debug = 0)

	cameraMatrix = numpy.array(camera_matrix).reshape((3,3))
	camera_params = (cameraMatrix[0,0], cameraMatrix[1,1], cameraMatrix[0,2], cameraMatrix[1,2])

	results = detector.detect(gray, True, camera_params, 0.1524)

#	for r in results:
#		(ptA, ptB, ptC, ptD) = r.corners
#		ptB = (int(ptB[0]), int(ptB[1]))
#		ptC = (int(ptC[0]), int(ptC[1]))
#		ptD = (int(ptD[0]), int(ptD[1]))
#		ptA = (int(ptA[0]), int(ptA[1]))

#		cv2.line(frame, ptA, ptB, (0, 255, 0), 2)
#		cv2.line(frame, ptB, ptC, (0, 255, 0), 2)
#		cv2.line(frame, ptC, ptD, (0, 255, 0), 2)
#		cv2.line(frame, ptD, ptA, (0, 255, 0), 2)

#		(cX, cY) = (int(r.center[0]), int(r.center[1]))
#		cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

#		tagFamily = r.tag_family.decode("utf-8")
#		cv2.putText(frame, tagFamily, (ptA[0], ptA[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#		print("[INFO] tag family: {}".format(tagFamily))
#		print("Tag ID: {}".format(r.tag_id))

	cv2.imshow("camera POV", frame)

	k = cv2.waitKey(1)

	if k%256 == 27:
		break # wait for ESC key to exit

cam.release()
cv2.destroyAllWindows()
