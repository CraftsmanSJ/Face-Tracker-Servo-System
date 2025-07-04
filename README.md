Face Tracking Servo Controller
This project uses Python, OpenCV, and MediaPipe to detect a human face with your webcam and automatically move two servo motors (pan & tilt) connected to an ESP32 to keep the face centered.

 How it works
1️. Python script

Uses your webcam to detect a face in real-time.

Calculates where the face is in the frame.

Maps the face position to servo angles (0°–180°).

Smooths the motion so your servos don’t jitter.

Sends the angles to the ESP32 over USB as plain text like 90,120\n.

2️. ESP32

Reads the angles from the serial port.

Moves two servo motors to follow the face smoothly.

What you need
1 × ESP32 board

2 × Servo motors (SG90 or similar)

External 5V power supply for servos (recommended)

Jumper wires

A webcam

How to use:
1. Install Python libraries
Run in terminal:

bash
Copy
Edit
pip install opencv-python mediapipe pyserial

2️. Flash the Arduino code

Open ESP32_FaceTracker.ino in Arduino IDE.

Connect your servos:

Servo X → GPIO 18

Servo Y → GPIO 19

Upload the sketch to your ESP32.

Open Serial Monitor at 9600 baud — you should see:

mathematica
Copy
Edit
ESP32 Face Tracker Ready - Plain Format
3️. Run the Python script
Make sure your ESP32 shows up as COM4 (or change COM4 in the script to your port).

Run:

bash
Copy
Edit
python facetracker.py
A window will open — your face should be tracked and the servos will follow you.

Tip
Press Q to quit.

Make sure your servos have enough power — don’t power them directly from the ESP32 3.3V or USB. Use a separate 5V source and connect grounds together.