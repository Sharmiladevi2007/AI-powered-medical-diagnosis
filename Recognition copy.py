import cv2
import dlib
import numpy as np
import pickle
import os

detector=dllib.get_frontal_face_detector()
predictor=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
face_recognizer=dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

encoding_dir='face_encodings'

def load_enodings():
    encodings = {}
    for filename in os.listdir(encoding_dir):
        ifilename.endswith('pkl'):
            name=filename.split('.')[0]
            with open (os.path.join(encoding_dir,filename),'rb')as f:
                encoding=pickle.load(f)
                encodings[name]=encoding
    return ncodings

def recognize_face():
    encodings=load_encodings()
    cap = cv2.VideoCapture(0)


    while True:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR.BGR2GRAY)
        faces=detector(gray)

        for face in faces:
            landmarks= predictor(gray,face)
            face_descriptor = face_recognizer.compute_face_descriptor(frame,landmarks)
            encoding=np.array(face_descriptor)

            matches={}
            for name,known_encoding in encodings.items():
                distance = np.linalg.norm(encoding-known_encoding)
                matches[name]=distance

            matched_name = min(matches,key=matches.get) 
            cv2.putText(frame, f"recgnized: {matched_name}",(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, )0, 255, 0), 2)

        cv2.imshow("FaceRecognition",frame)

        if cv2.waitkey(1) & 0xFF == ord('q'):
            break

    cap.realease()
    cv2.destroyAllWindows()

recognize_face()
