#include <Wire.h>
char empfangen = 0;
void setup()
{
  Wire.begin(4);
  Wire.onReceive(empfangen);
  Serial.begin(9600);  
}

void loop()
{
 delay(100);  
}

    Serial.println(empfangen);
}
