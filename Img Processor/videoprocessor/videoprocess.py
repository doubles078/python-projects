import cv2, time


#0 represents the index of the webcams.  I only have 1 webcam so the index is 0
video=cv2.VideoCapture(0)

count = 1

while True:
    check, frame = video.read()

    #lets count the amount of frames generated
    count = count+1

    print(check)
    print(frame)

    #time.sleep(3)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    #change the number value to increse or decrease frames captured
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

print(count)
video.release()
cv2.destroyAllWindows
