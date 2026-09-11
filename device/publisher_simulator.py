"""
无硬件模拟器 - 模拟ESP32每3秒上报一次温湿度
用途：没有ESP32开发板时，用它跑通整条链路
运行: python device/publisher_simulator.py
"""
import json
import random
import time
import datetime
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
DEVICE_ID = "esp32-sim-001"
TOPIC = f"iot/devices/{DEVICE_ID}/data"

# 初始温湿度（之后随机游走，更接近真实传感器）
temp = 24.0
hum = 55.0


def on_connect(client, userdata, flags, rc):
    print(f"模拟器已连接 Broker，返回码: {rc}")


client = mqtt.Client(client_id="iot-sim-publisher")
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

print(f"开始模拟设备 {DEVICE_ID} 上报（每3秒一次，Ctrl+C停止）...")
try:
    while True:
        # 随机游走：模拟真实环境的缓慢变化
        temp = round(temp + random.uniform(-0.3, 0.3), 1)
        hum = round(hum + random.uniform(-1.0, 1.0), 1)
        payload = {"temperature": temp, "humidity": hum}
        client.publish(TOPIC, json.dumps(payload))
        print(f"[{datetime.datetime.now():%H:%M:%S}] {TOPIC} -> {payload}")
        time.sleep(3)
except KeyboardInterrupt:
    print("\n模拟器已停止")
    client.loop_stop()
    client.disconnect()
