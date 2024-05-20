#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Asterix 2";
const char* password = "BL240774";

// Configura la URL del servidor o la IP
const char* serverUrl = "http://192.168.1.8:8000/devices";

#define SLAVE_ADDRESS 0x55

void setup() {
  Wire.begin();
  Serial.begin(115200);
  while (!Serial)
    ;
  Serial.println("Iniciando I2C maestro...");


  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
}

void loop() {
  byte response = ACKCommand('A');
  String payload;
  if (response != 'a') {
    Serial.println("Sensor desligado");
    payload = "{\"device\":\"esp32\",\"sensor_1\":\"desligado\",\"sensor_2\":\"none\",\"sensor_3\":\"none\"}";
  } else {
    Serial.println("Sensor ligado");
    payload = "{\"device\":\"esp32\",\"sensor_1\":\"ligado\",\"sensor_2\":\"none\",\"sensor_3\":\"none\"}";
  }
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");
    int httpResponseCode = http.POST(payload);
    Serial.print("Código de respuesta: ");
    Serial.println(httpResponseCode);
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("Respuesta del servidor: ");
      Serial.println(response);
    } else {
      Serial.print("Error en la solicitud: ");
      Serial.println(http.errorToString(httpResponseCode).c_str());
    }
    http.end();
  } else {
    Serial.println("Error de conexión WiFi");
  }
}

byte ACKCommand(byte command) {
  Wire.beginTransmission(SLAVE_ADDRESS);
  Wire.write(command);
  byte error = Wire.endTransmission();

  if (error == 0) {
    Wire.requestFrom(SLAVE_ADDRESS, 1);
    if (Wire.available()) {
      byte response = Wire.read();
      return response;
    }
  }
  return 0xff;
}
