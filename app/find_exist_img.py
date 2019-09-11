import os
import face_recognition
import cv2

known_face_encodes = []
known_face_names = []

def encode_face(filename=None):
    # 提取照片中最明显的人脸并进行特征提取, 如果输入照片为空则打开摄像机取照片
    if filename is not None:
        image = cv2.imread(filename)
    else:
        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)
        print("press the space or enter if ready!")
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()
            # Display the resulting image
            cv2.imshow('Video', frame)
            k = cv2.waitKey(1)
            if k in [13, 32]: # enter or space
                break
            # else:
            #     print("you pressed %d " % k)
        # Convert the image from BGR color (which OpenCV uses) to RGB color
        # (which face_recognition uses)
        image = frame # [:, :, ::-1]  # mac unnecessary
        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    top, right, bottom, left = face_locations[0]
    face_img = image[top:bottom, left:right, :]
    face_encode = face_encodings[0]
    return face_encode, face_img

def list_file(filedir, sufix=None):
    # 根据输入的后缀来列举文件夹中的文件
    file_list = os.listdir(filedir)
    file_list = [filedir + f for f in file_list] # add path for files
    if sufix is not None:
        ret_list = [f for f in file_list if f.endswith(sufix)]
        return ret_list
    else:
        return file_list


def load_faces_img(dirname):
    # 从人脸图像加载人脸数据
    for img_file in list_file(dirname, '.jpg'):
        known_face_names.append(img_file.split("/")[-1].split(".")[0])
        known_face_encode = encode_face(img_file)
        known_face_encodes.append(known_face_encode)
    print(known_face_encodes, known_face_names)

if __name__ == "__main__":
    load_faces_img("F:/MyPaper/upload/")
