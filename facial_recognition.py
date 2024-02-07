import cv2
import os
import uuid

class FaceDetector:
    def __init__(self, save_path="saved_faces"):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.save_path = save_path
        if not os.path.exists(save_path):
            os.makedirs(save_path)

    def detect_and_save_faces(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face_filename = f"{self.save_path}/{uuid.uuid4()}.jpg"
            cv2.imwrite(face_filename, face)

        return faces

def start_real_time_detection():
    detector = FaceDetector()
    cap = cv2.VideoCapture(0)

    frame_rate = 30  # assuming 30 fps
    detect_interval = 2  # detect every 2 seconds
    frame_count = 0

    

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        frame_count += 1
        if frame_count >= (frame_rate * detect_interval):
            frame_count = 0
            # Perform face detection
            faces = detector.detect_and_save_faces(frame)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Real-Time Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

