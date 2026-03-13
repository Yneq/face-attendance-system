import face_recognition
import cv2
import pickle
import csv
from datetime import datetime

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    names = []

    for encoding in encodings:

        matches = face_recognition.compare_faces(
            data["encodings"], encoding)

        name = "Unknown"

        if True in matches:
            matchedIdx = matches.index(True)
            name = data["names"][matchedIdx]

            with open("attendance.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([name, datetime.now()])

        names.append(name)

    for ((top, right, bottom, left), name) in zip(boxes, names):

        cv2.rectangle(frame, (left, top),
                      (right, bottom), (0, 255, 0), 2)

        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 0), 2)

    cv2.imshow("Face Attendance", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()