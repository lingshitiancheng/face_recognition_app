
import face_recognition
import os
import cv2


g = os.walk(r"F:/MyPaper/upload") # image路径

known_faces = []
known_face_encodings_list = []
known_face_encodings = []  # 人脸编码

def detect_face():
    for root,dirnames, filenames in g:
        for file_name in filenames:
            known_faces.append(file_name)
            known_face_encodings.append(face_recognition.face_encodings(file_name))

        for known_face in known_faces:
            img = cv2.imread(known_face)
            known_face_encodings = face_recognition.face_encodings(img)[0]
            known_face_encodings_list.append(known_face_encodings)
            print(known_face_encodings_list)

    # return known_faces,known_face_encodings_list





if __name__ == "__main__":
    detect_face()
