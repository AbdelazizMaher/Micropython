#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

byte numbers[10] = { 
                    B1111110, B0110000, B1101101, B1111001, B0110011, 
                    B1011011, B1011111, B1110000, B1111111, B1110011 
                    };
int inc_input_value;
int counter = 0;
bool go_by_switch = true;
int last_input_value = LOW;
int dec_input_value;
int reset_input_value;



// Handle received and sent messages
String message = "";
char incomingChar;



void setup() {
  pinMode(23, OUTPUT);
  pinMode(16, OUTPUT);
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(21, OUTPUT);
  pinMode(22, OUTPUT);

  Serial.begin(115200); 
  SerialBT.begin("ESP32");
  Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {


  if (SerialBT.available()){
    char incomingChar = SerialBT.read();
    if (incomingChar != 'k'){
      message += String(incomingChar);
    

    }
    else{
      message = "";
    }
    Serial.write(incomingChar);
      
  }


    
   if(go_by_switch) {
        if (message =="inc"){
        
            counter = (counter + 1) % 10;
        }
        
        delay(20);
    } 
    writeNumber(counter);

 
 
   
    if(go_by_switch) {
        if (message =="dec"){
        
            counter = (counter - 1) % 10;
        }
        delay(20);
    } 
    writeNumber(counter);



     if(go_by_switch) {
        if (message =="res"){
        
            counter = 0;
        }
        delay(20);
    } 
    writeNumber(counter);

}


void writeNumber(int number) {
  int segments[] = {23,16,17,18,19,21,22};
    if(number < 0 || number > 9) {
        return;
    }
    byte mask = numbers[number];
    byte currentPinMask = B1000000;
    for(int i = 0; i < 7; i++) { if(mask & currentPinMask) digitalWrite(segments[i],HIGH); else digitalWrite(segments[i],LOW); currentPinMask = currentPinMask >> 1;
    }

}
