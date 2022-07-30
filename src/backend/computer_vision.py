import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
    while webcam.isOpened():
        success, image = webcam.read()
        if not success:
            print('Empty camera frame')
            continue

        results = holistic.process(image)

        # Drawing the landmarks
        image.flags.writeable = True
        mp_drawing.draw_landmarks(
            image,
            results.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_contours_style())

        cv2.imshow('Gabi', image)
        # 27 is the ASCII code for the key 'Esc'
        if cv2.waitKey(5) == 27:
            break

webcam.release()