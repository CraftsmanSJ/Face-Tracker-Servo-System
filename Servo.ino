#include <ESP32Servo.h>

Servo servoX;
Servo servoY;

String inputString = "";
bool newData = false;

void setup() {
  Serial.begin(9600);

  servoX.attach(18);
  servoY.attach(19);

  servoX.write(90);
  servoY.write(90);

  Serial.println("ESP32 Face Tracker Ready - Plain Format");
}

void loop() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      newData = true;
      break;
    }
    inputString += inChar;
  }

  if (newData) {
    int commaIndex = inputString.indexOf(',');
    if (commaIndex > 0) {
      int angleX = inputString.substring(0, commaIndex).toInt();
      int angleY = inputString.substring(commaIndex + 1).toInt();

      angleX = constrain(angleX, 0, 180);
      angleY = constrain(angleY, 0, 180);

      servoX.write(angleX);
      servoY.write(angleY);

      Serial.print("X: ");
      Serial.print(angleX);
      Serial.print(" Y: ");
      Serial.println(angleY);
    } else {
      Serial.print("Invalid input: ");
      Serial.println(inputString);
    }

    inputString = "";
    newData = false;
  }
}
