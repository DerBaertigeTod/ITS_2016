#include <DmxSimple.h>
int incomingByte;

void setup() {

  Serial.begin(9600);
  
}


void loop() {
  if (Serial.available() > 0) {

    incomingByte = Serial.read();

    if (incomingByte == '1')
    {
       DmxSimple.write(1,0);
       DmxSimple.write(2,255);
       DmxSimple.write(3,255);
       DmxSimple.write(4,255);
      Serial.println("LED ist eingeschaltet!");
    } 

    if (incomingByte == '0')
    {
       DmxSimple.write(1,0);
       DmxSimple.write(2,0);
       DmxSimple.write(3,0);
       DmxSimple.write(4,0);
      Serial.println("LED ist ausgeschaltet!");
    }
  }
}
