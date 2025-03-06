import cv2
import dlib
import numpy as np
import od 
import pickle

detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_recognizer=dlib.face-recognition_model_v1('dlib_face_recogntiton_resnet_model_v1,dat')

encoding_dir='face_encodings'

if not os.path.exists(encoing_dir):
    os.makedirs(encoding_dir)

def save_encoding(name, encoding):
    file_path=os.path.join(encoding_dir,f"{name}.pkl")
    with open(file_oath, 'wb')af:
        pickle.dump(encoding,f)
        print(f'Encoding for {name} saved!")

def register_face(name):
    cap=cv2.Videocapture(0)
    print("Press 'q' to capture face image for registration.")


    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BDR2GRAY)
        faces=detector(gray)

        for face in faces:
            landmarks=predictor(gray,face)
            face_descriptor=face_recogniser.compute_face_description(frame.landmarks)
            encoding=np.array(face_descriptor)

            x,y,w,h=(face.left(),face.top(),face_width(),face_height())
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0, 255, 0) 2)

            cv2.puttext(frame, f"press 'q' to register {name}'s face", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

            cv2.imshow("Face registration".frame)

            if cv2.waitkey(1) &0xFF ==ord('q'):
                save_encoding(name, encoding
                break

            cap.release()
            cv2.destroyAllWindows()


user_name= input("Enter your name for registration:")
register_face(user_name)
            
