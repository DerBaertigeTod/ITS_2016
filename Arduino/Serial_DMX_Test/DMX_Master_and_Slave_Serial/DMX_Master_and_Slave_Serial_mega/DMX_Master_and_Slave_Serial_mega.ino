
#include <Conceptinetics.h>
#include <DmxSimple.h>

int channels_with_vals[128] = {0};

int number_of_channels = 128;

#define DMX_SLAVE_CHANNELS   number_of_channels
#define INPUT_SIZE ((number_of_channels*3)+number_of_channels)
DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void receiving() {
  digitalWrite(2, LOW);

    for (int i = 1; i <= number_of_channels; i++) {
          Serial.print(dmx_slave.getChannelValue(i));
          
          Serial.print(",");
    }
    Serial.println(" ");
  }

void sending() {
  digitalWrite(2, HIGH);
  for (int i = 0; i <= sizeof(channels_with_vals); i++) {
    DmxSimple.write( i+1, channels_with_vals[i] );
  }

}


void read_values() {
  char input[INPUT_SIZE + 1];
  byte size = Serial.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;
  int channelid = 0;
  char* command = strtok(input, "&");
  while (command != 0)
  {
    byte value = atoi(command);
    channels_with_vals[channelid] = (int) value;
    // Find the next command in input string
    command = strtok(0, "&");
    channelid++;
  }
    sending();
    
}

void setup() {
  pinMode(2, OUTPUT);
  DmxSimple.usePin(2);

  //set SoftwareSerial
  
  DmxSimple.maxChannel(number_of_channels);
  dmx_slave.enable();
  dmx_slave.setStartAddress (1);
  Serial.begin(115200);
  Serial.setTimeout(250);
  Serial.println("HY PI I'm Version 3");

}
void loop() {

  if (Serial.available() > 0) {
    read_values();
  }
  else {
    receiving();
  }

}
