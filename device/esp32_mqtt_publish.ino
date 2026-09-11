/*
 * ESP32 + DHT11 温湿度上报到MQTT Broker
 * 硬件接线：DHT11数据脚接GPIO4，VCC接3.3V，GND接GND
 *
 * Arduino IDE 准备：
 * 1. 文件->首选项->附加开发板管理器网址填入:
 *    https://espressif.github.io/arduino-esp32/package_esp32_index.json
 * 2. 工具->开发板->开发板管理器 搜索 esp32 安装
 * 3. 工具->管理库 搜索并安装: PubSubClient、DHT sensor library
 */
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHT_PIN 4
#define DHT_TYPE DHT11
DHT dht(DHT_PIN, DHT_TYPE);

// ===== 改成你自己的WiFi=====
const char* ssid = "你的WiFi名";
const char* password = "你的WiFi密码";
// ===========================

const char* mqtt_server = "broker.emqx.io";
const char* device_id = "esp32-001";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("连接WiFi");
  while (WiFi.status() != WL_CONNECTED) { delay(500); Serial.print("."); }
  Serial.println(" WiFi连接成功");

  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    while (!client.connected()) {
      client.connect(device_id);
      delay(500);
    }
  }
  client.loop();

  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  if (!isnan(temp) && !isnan(hum)) {
    String payload = "{\"temperature\":" + String(temp) +
                     ",\"humidity\":" + String(hum) + "}";
    String topic = "iot/devices/" + String(device_id) + "/data";
    client.publish(topic.c_str(), payload.c_str());
    Serial.println("上报: " + payload);
  }
  delay(5000);  // 5秒上报一次
}
