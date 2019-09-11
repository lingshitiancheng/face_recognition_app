import face_recognition
from app.find_exist_img import *

def detect_faces_in_image(file_stream):
    image = cv2.imread(file_stream)
    unknow_face_locations = face_recognition.face_locations(image)
    unknow_face_encodings = face_recognition.face_encodings(image, unknow_face_locations)
    top, right, bottom, left = unknow_face_locations[0]
    unknow_face_img = image[top:bottom, left:right, :]
    unknow_face_encode = unknow_face_encodings[0]

    for known_face_encode in known_face_encodes:
        match_results = face_recognition.compare_faces([known_face_encode],unknow_face_encode[0])
        if match_results[0]:
            return True



if __name__ == "__main__":
    img = face_recognition.load_image_file("01.jpg")
    detect_faces_in_image(img)

