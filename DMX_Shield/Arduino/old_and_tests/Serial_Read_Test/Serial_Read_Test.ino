

#include <Conceptinetics.h>
#include <SoftwareSerial.h>
#include <DmxSimple.h>
SoftwareSerial mySerial(10, 11); // RX, TX
int channels_with_vals[129];
const int number_of_channels = 128;

#define DMX_SLAVE_CHANNELS   number_of_channels


int INPUT_SIZE ((number_of_channels*3)+number_of_channels);
DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void initalisierung() {
  DmxSimple.maxChannel(number_of_channels);
  dmx_slave.enable();
  dmx_slave.setStartAddress (1);
}

void receiving() {
  digitalWrite(2, LOW);

    for (int i = 1; i <= number_of_channels; i++) {
          mySerial.print(dmx_slave.getChannelValue(i));
          
          mySerial.print(",");
    }
    mySerial.println(" ");
  }

void sending() {
  digitalWrite(2, HIGH);
  for (int i = 1; i < (sizeof(channels_with_vals)/sizeof(int)); i++) {
    mySerial.print(i);
    mySerial.print(':');
    mySerial.println(channels_with_vals[i]);  
  }
    mySerial.print("Input Size was:");
    mySerial.println(INPUT_SIZE);
   INPUT_SIZE = INPUT_SIZE+1;
}


void read_values() {
  char input[INPUT_SIZE + 1];
  byte size = mySerial.readBytes(input, INPUT_SIZE);
  // Add the final 0 to end the C string
  input[size] = 0;
  int channelid = 1;
  char* command = strtok(input, "&");
  while (command != 0)
  {
    int value = atoi(command);
    channels_with_vals[channelid] = value;
    // Find the next command in input string
    command = strtok(0, "&");
    channelid++;
  }
    sending();
    delay(3000);
}

void setup() {
  pinMode(2, OUTPUT);
  DmxSimple.usePin(3);
  //set SoftwareSerial
  mySerial.begin(115200);
  mySerial.setTimeout(1000);
  initalisierung();
  mySerial.println("HY PI I'm Version 3");
  sending();

}
void loop() {

  if (mySerial.available() > 0) {
    read_values();
  }
 }
