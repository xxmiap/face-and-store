import cv2
import numpy as np
from keras.models import load_model

class FaceNetRecognizer:
    def __init__(self, model_path):
        self.model = load_model(model_path)
        self.face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def preprocess_face(self, face):
        face = cv2.resize(face, (160, 160))  # Resize to 160x160
        face = face.astype('float32')  # Convert pixel values to float
        mean, std = face.mean(), face.std()
        face = (face - mean) / std  # Normalize the face
        face = np.expand_dims(face, axis=0)  # Add batch dimension
        return face

    def get_embedding(self, face):
        face = self.preprocess_face(face)
        embedding = self.model.predict(face)
        return embedding[0]  # Assuming model returns batch predictions

    def detect_faces(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return faces

    def recognize_face(self, frame):
        faces = self.detect_faces(frame)
        for (x, y, w, h) in faces:
            face_image = frame[y:y+h, x:x+w]
            embedding = self.get_embedding(face_image)

            # Compare embedding with those in the database
            # For now, just print the embedding
            print("Embedding:", embedding)


    def recognize_or_store_face(self, frame, db_manager):
        faces = self.detect_faces(frame)
        for (x, y, w, h) in faces:
            face_image = frame[y:y+h, x:x+w]
            embedding = self.get_embedding(face_image)

            if db_manager.is_new_face(embedding):
                # Save the new face and its embedding to the database
                db_manager.save_new_face(face_image, embedding)
                print("New face stored.")
            else:
                print("Face already exists in the database.")


