import cv2, time

video = cv2.VideoCapture(0)
frameCount = 1
check, frame = video.read()

while True:
    frameCount += 1
    # print(check)
    # print(frame)
    # time.sleep(3)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1000)

    if key == ord('q'):
        break

print(frameCount)
video.release()
cv2.destroyAllWindows()
