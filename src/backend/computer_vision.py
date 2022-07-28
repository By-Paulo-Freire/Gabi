import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

detect = mp.solutions.face_detection
face_detection = detect.FaceDetection()
draw_box = mp.solutions.drawing_utils

while True:
    # webcam.read gives back two parameters
    detected, frame = webcam.read()

    if not detected:
        break

    faces = face_detection.process(frame)

    if faces.detections:
        for face in faces.detections:
            draw_box.draw_detection(frame, face)

    cv2.imshow('teste', frame)
    # 27 is the ASCII code for the key 'Esc'
    if cv2.waitKey(5) == 27:
        break

webcam.release()