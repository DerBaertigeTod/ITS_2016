#include <DmxSimple.h>
int rot = 3;  //Lesen
int valrot = 0;  // Auswertung
int gruen = 1;  //Lesen
int valgruen = 0;  // Auswertung
int blau = 2;  //Lesen
int valblau = 0;  // Auswertung
int R = 0;
int G = 0;
int B = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  valrot = analogRead(rot);   //Wert ausgeben
  Serial.println("Wert: ");
  Serial.println(valrot);
  
    valgruen = analogRead(gruen);   //Wert ausgeben
  Serial.println("Wert: ");
  Serial.println(valgruen);
  
    valblau = analogRead(blau);   //Wert ausgeben
  Serial.println("Wert: ");
  Serial.println(valblau);
  //delay(500);

R = 0;
G = valgruen/4;
B = valblau/4;
DmxSimple.write(2, R);
DmxSimple.write(84, G);
DmxSimple.write(83, B);
DmxSimple.write(3, G);
DmxSimple.write(4, B);


}

