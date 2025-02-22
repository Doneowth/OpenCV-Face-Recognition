''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc                       

Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18    

'''
import time

import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cat_face_detector = cv2.CascadeClassifier('haarcascade_frontalcatface_default.xml')

# For each person, enter one numeric face id
# face_id = input('\n enter user id end press <return> ==>  ')
time.sleep(4)
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

# merge
# for hi cat and don  merge merge merge 2
# b
# c
# for hi cat and don  merge merge
# a
# b
while True:
    ret, img = cam.read()
    # time.sleep(5)

    # img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # for (x, y, w, h) in faces:
    #
    #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     count += 1

        # Save the captured image into the datasets folder
        # cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        # cv2.imwrite("machi/Cat." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])

    cv2.imshow('image', img)

    # Press 'ESC' for exiting video
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


