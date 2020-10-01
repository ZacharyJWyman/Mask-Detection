import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

while True:
    
    check, frame = video.read()

    cv2.imshow('Face Detector', frame)
    key= cv2.waitKey(1)
    
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
            
    