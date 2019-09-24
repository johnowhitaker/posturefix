#import required libraries
import cv2
import time
import pymsgbox

#point to the haar cascade file in the directory
cascPath = "haarcascade.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

#start the camera
video_capture = cv2.VideoCapture(0)

#give camera time to warm up
time.sleep(0.1)

slouch = False
t_last = time.time()

#start video frame capture loop
while True:
    # take the frame, convert it to black and white, and look for facial features
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # use appropriate flag based on version of OpenCV
    if int(cv2.__version__.split('.')[0]) >= 3:
        cv_flag = cv2.CASCADE_SCALE_IMAGE
    else:
        cv_flag = cv2.cv.CV_HAAR_SCALE_IMAGE

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv_flag
    )

    #for each face, draw a green rectangle around it and append to the image
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if y > 250:
            print('slouch')
            slouch = True
        else:
            slouch=False
    if slouch == True and time.time()-t_last > 10:
        pymsgbox.alert('Stop Slouching!', 'PostureFix')
        t_last = time.time()

    #display the resulting image
    cv2.imshow('PostureFix', frame)

	#set "q" as the key to exit the program when pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
    time.sleep(1)

# clear the stream capture
video_capture.release()
cv2.destroyAllWindows()
