int aPin = 2;  //                     A
int bPin = 3;  //             ________
int cPin = 4;  //           |                   |
int dPin = 5;  //       F  |                   |  B
int ePin = 6;  //           |         G       |
int fPin = 7;  //            |________|
int gPin = 8;  //           |                   |
int GND1 = 9;  //        |                   |
int GND2 = 10; //   E |                   |   C
int GND3 = 11; //       |________|
int GND4 = 12; //       
int num;       //         D
int dig1 = 0;
int dig2 = 0;
int dig3 = 0;
int dig4 = 0;
int DTime = 4;

void setup()
{
  pinMode(aPin, OUTPUT);
  pinMode(bPin, OUTPUT);
  pinMode(cPin, OUTPUT);
  pinMode(dPin, OUTPUT);
  pinMode(ePin, OUTPUT); 
  pinMode(fPin, OUTPUT);
  pinMode(gPin, OUTPUT);
  pinMode(GND1, OUTPUT);
  pinMode(GND2, OUTPUT);
  pinMode(GND3, OUTPUT);
  pinMode(GND4, OUTPUT);
  Serial.begin(9600);
}



void loop()
{
  digitalWrite( GND1, HIGH);
  digitalWrite( GND2, HIGH);
  digitalWrite( GND3, HIGH);
  digitalWrite( GND4, HIGH);

  digitalWrite(  2, HIGH); // A
  digitalWrite(  3, HIGH); // B
  digitalWrite(  4, HIGH); // C
  digitalWrite(  5, HIGH); // D
  digitalWrite(  6, HIGH); // E
  digitalWrite(  7, HIGH); // F
  digitalWrite(  8, LOW); // G
}
