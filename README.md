# IoT-Application-Demo

> 📝 **图文教程（完整踩坑实录）**：[专科零基础跑通物联网全链路：ESP32+MQTT+Flask 实时监控看板（含4个新手必踩的坑）](https://blog.csdn.net/2401_85632023/article/details/165103564) —— 保姆级讲解 + 4个新手必踩坑的解决方案

一个从零搭建的物联网应用 Demo：**设备(ESP32/模拟器) → MQTT → Python后端 → Flask + WebSocket → ECharts实时看板**

## 项目架构

```
[ESP32 / 模拟器] --MQTT--> [broker.emqx.io] --MQTT--> [mqtt_subscriber.py]
                                                            |
                                                            v (内存队列)
                                                      [app.py Flask]
                                                            |
                                                            v (WebSocket)
                                                      [dashboard.html 实时曲线]
```

## 快速开始（无硬件版）

```bash
# 1. 安装依赖（建议先创建虚拟环境）
pip install -r requirements.txt

# 2. 终端1：启动Web服务
python backend/app.py

# 3. 终端2：启动数据模拟器（代替真实ESP32）
python device/publisher_simulator.py

# 4. 浏览器打开
http://localhost:5000
```

看到温度曲线每3秒跳动一次，说明整条链路跑通了。

## 有硬件版（ESP32 + DHT11）

接线：DHT11 数据脚 → GPIO4，VCC → 3.3V，GND → GND

1. Arduino IDE 安装 ESP32 开发板支持
2. 安装库：PubSubClient、DHT sensor library
3. 修改 `device/esp32_mqtt_publish.ino` 里的 WiFi 名和密码
4. 上传到 ESP32，看板自动出现新设备

## 目录结构

```
IoT-Application-Demo/
├── README.md               # 本文件
├── LICENSE                 # MIT
├── .gitignore
├── requirements.txt        # Python依赖
├── device/                 # 设备端
│   ├── esp32_mqtt_publish.ino    # ESP32真实代码
│   ├── publisher_simulator.py    # 无硬件模拟器
│   └── README.md
├── backend/                # 后端
│   ├── mqtt_subscriber.py  # MQTT订阅器（核心）
│   ├── data_processor.py   # 数据统计
│   └── app.py              # Flask + WebSocket服务
├── frontend/               # 前端
│   └── templates/
│       └── dashboard.html  # ECharts实时看板
├── docs/
│   ├── setup_guide.md      # 部署文档
│   └── learning_notes.md   # 学习笔记
└── screenshots/            # 运行截图（作品集素材）
```

## 安全提示

- 使用的是公共免费 Broker（broker.emqx.io），**任何人都能订阅到你的数据**，不要发送任何真实/敏感信息
- 生产环境应替换为自己部署的 EMQX/Mosquitto，并开启用户名密码认证

## License

MIT
