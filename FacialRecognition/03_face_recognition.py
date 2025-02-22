''''
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18  

'''

import cv2
import time
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer_human.yml')
recognizer.read('trainer/trainer_cat.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cat_cascadePath = "haarcascade_frontalcatface_default.xml"
cat_faceCascade = cv2.CascadeClassifier(cat_cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Don', 'X', 'Machi', 'Z', 'W']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
time.sleep(2)

while True:
    ret, frame = cam.read()
    # img = cv2.flip(img, -1) # Flip vertically
    if frame is None:
        print("empty frame")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    cat_faces = cat_faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    human_name = "unknown human"
    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 100):
            confidence = "  {0}%".format(round(100 - confidence))
            # if id < len(names):
            #     human_name = names[id % 5]
            #     confidence = "  {0}%".format(round(100 - confidence))
            # else:
            #     print("index out of bounds human id: {}".format(id))

        else:
            human_name = "? human"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(frame, str("Don"), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cat_name = "unknown cat"
    # for (x, y, w, h) in cat_faces:
    #
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #     cid, confidence = recognizer.predict(gray[y:y + h, x:x + w])
    #
    #     # Check if confidence is less them 100 ==> "0" is perfect match
    #     if (confidence < 100):
    #         confidence = "  {0}%".format(round(100 - confidence))
    #         # if cid < len(names):
    #         #     cat_name = names[cid]
    #         #     confidence = "  {0}%".format(round(100 - confidence))
    #         # else:
    #         #     print("index out of bounds cat id: {}".format(cid))
    #
    #     else:
    #         cat_name = "? cat"
    #         confidence = "  {0}%".format(round(100 - confidence))

    #   cv2.putText(frame, str("DuoDuo"), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
    #   cv2.putText(frame, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', frame)

    # Press 'ESC' for exiting video
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
