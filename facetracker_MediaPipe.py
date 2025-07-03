import cv2 as cv
import mediapipe as mp

#initalizing the mediapipe
face_detector = mp.solutions.face_detection #for detecting faces

#opening the webcam
capture = cv.VideoCapture(0)

with face_detector.FaceDetection(model_selection = 0 , min_detection_confidence = 0.5) as detected_face :
    while True :
        isTrue , frame = capture.read()
        if not isTrue :
            break
        
        #converting the frame to RGB
        rgb_image = cv.cvtColor(frame , cv.COLOR_BGR2RGB)

        #processing the frame for getting the detections
        results = detected_face.process(rgb_image)

        #plotting the faces
        if results.detections :
            for detection in results.detections:
                heigth , width , _ = frame.shape
                box = detection.location_data.relative_bounding_box

                x = int(box.xmin*width)
                y = int(box.ymin*heigth)
                w = int(box.width * width)
                h = int(box.height*heigth)

                 #drawing a horizontal line
                cv.line(frame , (0,y+h//2) , (x+w//2 , y+h//2) , (0,0,0) , 2)
                cv.line(frame , (x+w//2 , y+h//2) , (frame.shape[1],y+h//2) , (0,0,0) , 2)

                #drawing the circle
                cv.circle(frame , (x+w//2 , y+h//2) , 5 , (0,0,255) , -1)
                cv.circle(frame , (x+w//2 , y+h//2) , 20 , (0,0,255) , 2)

                #drawing the vertical line
                cv.line(frame, (x + w//2, 0), (x + w//2, y + h//2), (0,0,0), 2)
                cv.line(frame , (x+w//2 , y+h//2) , (x+w//2 , frame.shape[0]) , (0,0,0) , 2)

        cv.imshow("Face Tracker" , frame)

        if cv.waitKey(20) & 0xFF == ord('q') :
            break

capture.release()
cv.destroyAllWindows()

    