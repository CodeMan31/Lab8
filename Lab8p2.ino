#include <Servo.h>
Servo servo1;
Servo servo2;
int pot1 = 0;
int pot2 = 1;

void setup() {
  // put your setup code here, to run once:
  servo1.attach(2);
  servo2.attach(3);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val1 = analogRead(pot1);
  int val2 = analogRead(pot2);

   val1 = map(val1, 0, 1023, -90, 90);
   val2 = map(val2, 0, 1023, -90, 90);
   servo1.write(val1);
   servo2.write(val2);
   delay(15);
   
}
