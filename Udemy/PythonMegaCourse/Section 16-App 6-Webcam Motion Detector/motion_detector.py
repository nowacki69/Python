import cv2, time, pandas
from datetime import datetime

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    status_list = []

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # Convert frame to grayscale
    gray = cv2GaussianBlue(gray, (21,21), 0)            # Blur frame

    if first_frame is None:                             # If 1st frame, go get another
        first_frame = gray
        continue

    delta_frame = cv2.absdif(first_frame, gray)         
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    (_, cnts, _) = cv2.findCountours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        
        status = 1
        (x, y, w, h) = cv2.boundRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

    status_list.append(status)
    if len(status_list) > 1:
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())
        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)

    ky = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

    for i in range(0, len(times), 2):
        df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True})

    df.to_csv("Times.csv")
    
    video.release()
    cv2.destroyAllWindows()
