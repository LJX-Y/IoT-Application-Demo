# device/ 设备端说明

## 两种方式二选一

| 方式 | 文件 | 适用 |
|---|---|---|
| 无硬件模拟 | `publisher_simulator.py` | 没有开发板，先用Python跑通链路 |
| 真实硬件 | `esp32_mqtt_publish.ino` | 有ESP32 + DHT11 |

## 模拟器（推荐先跑这个）

```bash
python device/publisher_simulator.py
```

每3秒模拟一次温湿度（随机游走），发布到 `iot/devices/esp32-sim-001/data`。

## 真实硬件清单（淘宝约25元）

- ESP32 开发板 ×1（约12元）
- DHT11 温湿度传感器 ×1（约5元，建议买带三针的模块版）
- 杜邦线母对母 ×3（约2元）
- Micro USB数据线 ×1

接线：
| DHT11 | ESP32 |
|---|---|
| VCC | 3.3V |
| GND | GND |
| DATA | GPIO4 |
