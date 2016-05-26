

#include <Conceptinetics.h>
#include <SoftwareSerial.h>
#include <DmxSimple.h>
SoftwareSerial mySerial(10, 11); // RX, TX
unsigned long       lastFrameReceivedTime;
const unsigned long dmxTimeoutMillis = 10000UL;
int channels_with_vals[] ={};
int number_of_channels = 256;

#define DMX_SLAVE_CHANNELS   number_of_channels 


#define INPUT_SIZE (((number_of_channels*3)+number_of_channels)*2)+1
DMX_Slave dmx_slave ( DMX_SLAVE_CHANNELS );



void initalisierung(){
   DmxSimple.maxChannel(number_of_channels);
   dmx_slave.enable();
   dmx_slave.setStartAddress (1);
  

   for (int i; i <= number_of_channels;i++){
     channels_with_vals[i] = 0;
   }
}

void receiving(){
  digitalWrite(13, LOW);
     
  for(int i=1;i<=DMX_SLAVE_CHANNELS;i++){
  mySerial.print(dmx_slave.getChannelValue(i) );
  mySerial.print(",");
  }
  mySerial.println(" ");
}
void sending(){
  digitalWrite(2, HIGH);
  for(int i=0;i<=number_of_channels;i++){
    DmxSimple.write( i, channels_with_vals[i] );
  }
    
}


void read_values(){ 
char input[INPUT_SIZE + 1];
 byte size = mySerial.readBytes(input, INPUT_SIZE);
// Add the final 0 to end the C string
input[size] = 0;
  char* command = strtok(input, "&");
  while (command != 0)
  {
      // Split the command in two values
      char* separator = strchr(command, ':');
      if (separator != 0)
      {
          // Actually split the string in 2: replace ':' with 0
          *separator = 0;
          int channelid = atoi(command);
          ++separator;
          int value = atoi(separator);
          channels_with_vals[channelid] == value;
      // Find the next command in input string
      command = strtok(0, "&");
    }
    sending();
    }
}

void setup() {             
 pinMode(2, OUTPUT);
 DmxSimple.usePin(3);
 
  //set SoftwareSerial
   mySerial.begin(115200);
   mySerial.setTimeout(100);
  initalisierung();
  
}
void loop(){
 
  if (mySerial.available() > 0) {
   read_values();
  }
  else{
    receiving();
  }
  
}

