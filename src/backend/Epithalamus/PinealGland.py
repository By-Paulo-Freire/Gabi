import cv2

Alive = True
webcam = cv2.VideoCapture(0)

while Alive:
    print('I am alive')
    if webcam:
        with open('./computer_vision.py', 'r') as f:
            code = f.read()
        exec(code)