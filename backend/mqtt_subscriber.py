"""
MQTT订阅服务 - 接收设备数据并存入内存队列
"""
import json
import paho.mqtt.client as mqtt
from queue import Queue
from datetime import datetime

# 数据队列（生产环境应替换为Redis/InfluxDB）
data_queue = Queue(maxsize=1000)


def on_connect(client, userdata, flags, rc):
    print(f"[{datetime.now():%H:%M:%S}] MQTT连接成功，返回码: {rc}")
    # 订阅所有设备数据（+ 是单层通配符，匹配任意设备ID）
    client.subscribe("iot/devices/+/data")


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        data = {
            "device_id": msg.topic.split("/")[2],
            "timestamp": datetime.now().isoformat(),
            "topic": msg.topic,
            **payload
        }
        data_queue.put(data)
        print(f"[{data['timestamp'][11:19]}] {data['device_id']}: "
              f"温度={data.get('temperature')} 湿度={data.get('humidity')}")
    except Exception as e:
        print(f"数据解析失败: {e}")


def start_mqtt_subscriber(broker="broker.emqx.io", port=1883):
    """启动MQTT订阅器（使用免费的公共Broker）"""
    client = mqtt.Client(client_id="iot-backend-subscriber")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.loop_start()  # 后台线程运行，不阻塞主程序
    return client


if __name__ == "__main__":
    print("启动MQTT订阅服务...")
    start_mqtt_subscriber()
    import time
    while True:
        time.sleep(1)
