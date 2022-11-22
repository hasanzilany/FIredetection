#include "SoftwareSerial.h"

SoftwareSerial serial_connection(10, 11);//Create a serial connection with TX and RX on these pins || OR SETUP FOR USB CONNECTION
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar = -1; //Initialie the first character as nothing
int count = 0; //This is the number of lines sent in from the python script
int i = 0; //Arduinos are not the most capable chips in the world so I just create the looping variable once
 



void setup()
{
  
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
  
void loop()
{
  //This will prevent bufferoverrun errors
  byte byte_count = serial_connection.available(); //This gets the number of bytes that were sent by the python script
  if (byte_count) //If there are any bytes then deal with them
  {
    if (serial_connection.read() == 's')
    {
     //print or buzzer setup
      delay(2000);
    }
  }


  delay(100);//Pause for a moment
}