import face_recognition
import os
from datetime import datetime

known_face_encodings = []
known_face_names = []

dataset_path = "../dataset"

for file in os.listdir(dataset_path):

    img = face_recognition.load_image_file(f"{dataset_path}/{file}")
    encoding = face_recognition.face_encodings(img)[0]

    known_face_encodings.append(encoding)
    known_face_names.append(file.split(".")[0])


def recognize_face(img_file):

    image = face_recognition.load_image_file(img_file)

    face_locations = face_recognition.face_locations(image)

    face_encodings = face_recognition.face_encodings(image, face_locations)

    for face_encoding in face_encodings:

        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_encoding
        )

        if True in matches:

            index = matches.index(True)

            name = known_face_names[index]

            return {
                "name": name,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    return {"name": "Unknown", "time": None}