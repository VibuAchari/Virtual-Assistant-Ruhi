# core/media.py

import pyautogui
import cv2
import time
import os

def take_screenshot(filename="screenshot.jpg"):
    time.sleep(5)
    pyautogui.screenshot().save(filename)

def take_picture():
    face_cascade = cv2.CascadeClassifier(os.path.join('resources', 'haarcascade_frontalface_alt.xml'))
    video = cv2.VideoCapture(0)
    video.set(3, 852)
    video.set(4, 480)
    image_counter = 0

    while True:
        check, frame = video.read()
        flipped_frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

        cv2.imshow("Ruhi Camera", flipped_frame)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break
        elif key == ord('s'):
            img_name = f"ruhi_capture{image_counter}.png"
            cv2.imwrite(img_name, flipped_frame)
            print(f"{img_name} captured!")
            image_counter += 1

    video.release()
    cv2.destroyAllWindows()
