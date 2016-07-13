#include <AltSoftSerial.h>



#include <Conceptinetics.h>
#include <DmxSimple.h>
#include <string.h>

int channels_with_vals[129];
const int number_of_channels = 128;

#define DMX_SLAVE_CHANNELS   number_of_channels


DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void initalisierung() {
  DmxSimple.maxChannel(number_of_channels);
  dmx_slave.enable();
  dmx_slave.setStartAddress (1);
  }

void receiving() {
  digitalWrite(2, LOW);

    for (int i = 1; i <= number_of_channels; i++) {
          Serial2.print(dmx_slave.getChannelValue(i));
          
          Serial2.print(",");
    }
    Serial2.println(" ");
  }

void sending() {
  digitalWrite(2, HIGH);
  for (int i = 1; i < (sizeof(channels_with_vals)/sizeof(int)); i++) {
    Serial2.print(i);
    Serial2.print(':');
    Serial2.println(channels_with_vals[i]);  
  }
    Serial2.print("Input Size was:");
   
}


void read_values() {
    String input = Serial2.readString();
    Serial2.println(input);
      
    //  sending();
  
}

void setup() {
  pinMode(2, OUTPUT);
  DmxSimple.usePin(3);
  //set SoftwareSerial
  Serial2.begin(115200);
  Serial2.setTimeout(50);
  initalisierung();
  Serial2.println("HY PI I'm Version 3");
  sending();

}
void loop() {

 if (Serial2.available() > 0) {
    read_values();
   
  }
 }
