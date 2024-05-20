#include <Wire.h>

#define SLAVE_ADDRESS 0x55
byte receivedCommand;
byte responseData;

void setup() {
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Iniciando I2C esclavo...");
}

void loop() {
}

void receiveEvent(int bytes) {
  while (Wire.available()) {
    receivedCommand = Wire.read();
    Serial.print("Comando recibido: ");
    Serial.println((char)receivedCommand);

    switch (receivedCommand) {
      case 'A':
        responseData = 'a';
        break;
      default:
        responseData = 0xFF;
        break;
    }
  }
}

void requestEvent() {
  Wire.write(responseData); 
}
