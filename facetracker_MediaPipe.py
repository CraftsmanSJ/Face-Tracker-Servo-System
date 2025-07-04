import cv2 as cv
import mediapipe as mp
import serial
import time
import numpy as np

# establish serial
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)
time.sleep(2)

# init mediapipe
face_detector = mp.solutions.face_detection
capture = cv.VideoCapture(0)

with face_detector.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detected_face:
    while True:
        isTrue, frame = capture.read()
        if not isTrue:
            print("Failed to grab frame")
            break

        rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = detected_face.process(rgb_image)

        if results.detections:
            for detection in results.detections:
                height, width, _ = frame.shape
                box = detection.location_data.relative_bounding_box

                x = int(box.xmin * width)
                y = int(box.ymin * height)
                w = int(box.width * width)
                h = int(box.height * height)

                cx = x + w // 2
                cy = y + h // 2

                servo_x = int((cx / width) * 180)
                servo_y = int((cy / height) * 180)

                servo_x = max(0, min(180, servo_x))
                servo_y = max(0, min(180, servo_y))

                # Draw overlay
                cv.line(frame, (0, y + h // 2), (x + w // 2, y + h // 2), (0, 0, 0), 2)
                cv.line(frame, (x + w // 2, y + h // 2), (frame.shape[1], y + h // 2), (0, 0, 0), 2)

                cv.circle(frame, (x + w // 2, y + h // 2), 5, (0, 0, 255), -1)
                cv.circle(frame, (x + w // 2, y + h // 2), 20, (0, 0, 255), 2)

                cv.line(frame, (x + w // 2, 0), (x + w // 2, y + h // 2), (0, 0, 0), 2)
                cv.line(frame, (x + w // 2, y + h // 2), (x + w // 2, frame.shape[0]), (0, 0, 0), 2)

                command = f"{servo_x},{servo_y}\n"
                print(f"x : {servo_x} , y : {servo_y}")
                try:
                    arduino.write(command.encode('utf-8'))
                except Exception as e:
                    print(f"Serial write error: {e}")

        cv.imshow("Face Tracker", frame)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break

capture.release()
cv.destroyAllWindows()
arduino.close()
