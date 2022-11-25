import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow("le camera POV")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break
    cv2.imshow("le camera POV", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "capture.png"
        cv2.imwrite(img_name, frame)
        print("Image written!")
        img_counter += 1

cam.release()

cv2.destroyAllWindows()