#define F_CPU 16000000UL
unsigned char X ='U';
void setup() {

Serial1.begin(115200);
 
  Serial1.println("HY PI I'm the AATmega162");
   pinMode(20, OUTPUT);

}

void loop() {
  delay(500);
  digitalWrite(20, LOW);
 Serial1.println("I'm a Test Message");
 delay(500);
  digitalWrite(20, HIGH);
 
}
