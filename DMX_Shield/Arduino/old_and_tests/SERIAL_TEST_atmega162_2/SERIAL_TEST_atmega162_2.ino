//#define F_CPU  18432000UL
void setup() {
  Serial1.begin(115200);
  Serial1.println("HY PI I'm the DMX_Serial Handler Version 3.1 SERIAL 1");
Serial.begin(115200);
  Serial.println("HY PI I'm the DMX_Serial Handler Version 3.1 SERIAL 0");
}

void loop() {
 Serial1.println("TEST on SERIAL 1");
 delay(1000);
 Serial.println("TEST on SERIAL 0");
 delay(1000);
}
