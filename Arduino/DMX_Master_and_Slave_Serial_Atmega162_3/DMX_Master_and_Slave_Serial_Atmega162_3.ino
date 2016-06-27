#include <Conceptinetics.h>
#define SERIAL_TX_BUFFER_SIZE 16
#define SERIAL_RX_BUFFER_SIZE 16
// Alle Variablen Definieren:
int number_of_channels = 64;
int channels_with_vals[64]={0};
#define DMX_SLAVE_CHANNELS   number_of_channels
#define DMX_MASTER_CHANNELS  number_of_channels
#define INPUT_SIZE ((number_of_channels*3)+number_of_channels)
#define RXEN_PIN                20

DMX_Master        dmx_master ( DMX_MASTER_CHANNELS, RXEN_PIN );
DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void setup() {
 dmx_slave.enable ();
 dmx_slave.setStartAddress (1);
 dmx_master.enable ();
 dmx_master.setChannelRange ( 1, 5, 50 );
 Serial.begin(115200,0x86);
 Serial.println("HY PI I'm the DMX_Serial Handler Version 5");
 
}



void receiving() {
  
    for (int i = 1; i <=number_of_channels; i++) {
          Serial.print(dmx_slave.getChannelValue(i));       
          Serial.print(",");
    }
    Serial.println(" ");
}

void sending() {
  for (int i = 1; i <= number_of_channels; i++) {
    dmx_master.setChannelValue(i, channels_with_vals[i]);
  }

}


void read_values() {
  char input[INPUT_SIZE + 1];
  byte size = Serial.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;
  Serial.print(input);
  int channelid = 1;
  char* command = strtok(input,"&");
  while (command != 0)
  {
    int value = atoi(command);
    //channels_with_vals[channelid] =  value;
    dmx_master.setChannelValue(channelid, value);
    command = strtok(0,"&");
    channelid++;
  }
    //sending();
}

void loop() {
  if (Serial.available() > 0) {
    read_values();
  }
  else {
   receiving();
  }
  
}
