import cv2
import mediapipe as mp
from deepface import DeepFace

webcam = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
human_tracking = 'false'

font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 255)

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
    while webcam.isOpened():
        success, image = webcam.read()
        if not success:
            print('Empty camera frame')
            continue

        results = holistic.process(image)
        attributes = ['age', 'gender', 'race', 'emotion']
         # Get the coordinates of the text
        org = (5, 50)


        try:
            df = DeepFace.analyze(image, attributes)
            human_tracking = 'true'
            print(df['age'], df['gender'], df['dominant_race'], df['dominant_emotion'], 'human_tracking')
            text = f"""
                Human Tracking:     {human_tracking}
                Guessed Age:        {df['age']}
                Guessed Gender:     {df['gender']}
                Guessed Race:       {df['dominant_race']}
                Guessed Emotion:    {df['dominant_emotion']}
                Objective:          KILL
                """
            # Add the text to the frame
            cv2.putText(image, text, org, font, 0.5, color, 2)
        except:
            human_tracking = 'false'
            #print('No face detected', human_tracking)
            pass

        cv2.imshow('Gabi', image)
        # 27 is the ASCII code for the key 'Esc'
        if cv2.waitKey(5) == 27:
            break

webcam.release()