#include <Conceptinetics.h>
#include <EEPROM.h>

// Alle Variablen Definieren:
unsigned int number_of_channels = 256;
byte channels_with_vals[256] = {0};
#define DMX_SLAVE_CHANNELS   number_of_channels
#define DMX_MASTER_CHANNELS  number_of_channels
#define INPUT_SIZE ((number_of_channels*3)+number_of_channels)
#define RXEN_PIN                2
DMX_Master        dmx_master ( DMX_MASTER_CHANNELS, RXEN_PIN );
DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );





void initalisierung() {
  dmx_slave.enable ();
  dmx_slave.setStartAddress (1);
  dmx_master.enable ();
  dmx_master.setChannelRange ( 1, 512, 0 );
}

void receiving() {
  digitalWrite(2, LOW);

    for (int i = 1; i <= number_of_channels; i++) {
          Serial1.print(dmx_slave.getChannelValue(i));       
          Serial1.print(",");
    }
    Serial1.println(" ");
}

void sending() {
  digitalWrite(2, HIGH);
  for (int i = 0; i <= sizeof(channels_with_vals); i++) {
    dmx_master.setChannelValue( i+1, ((int) channels_with_vals[i]) );
  }

}


void read_values() {
  char input[INPUT_SIZE + 1];
  byte size = Serial1.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;
  int channelid = 0;
  char* command = strtok(input, "&");
  while (command != 0)
  {
    int value = atoi(command);
    channels_with_vals[channelid] = (byte) value;
    // Find the next command in input string
    command = strtok(0, "&");
    channelid++;
  }
    sending();
}

void setup() {
  Serial1.begin(115200);
  Serial1.setTimeout(250);
  initalisierung();
  Serial1.println("HY PI I'm the DMX_Serial Handler Version 3.1");

}
void loop() {

  if (Serial1.available() > 0) {
    read_values();
  }
  else {
    receiving();
  }

}
