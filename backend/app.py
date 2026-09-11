"""
Web可视化服务 - 实时显示设备数据
运行: python backend/app.py
浏览器打开 http://localhost:5000
"""
from flask import Flask, render_template
from flask_socketio import SocketIO
from mqtt_subscriber import start_mqtt_subscriber, data_queue

# 模板和静态文件在 frontend/ 目录下
app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")
app.config['SECRET_KEY'] = 'iot-demo-secret'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')


@app.route('/')
def index():
    return render_template('dashboard.html')


# 后台线程：从MQTT队列读取数据，通过WebSocket推送到前端
def background_thread():
    while True:
        if not data_queue.empty():
            data = data_queue.get()
            socketio.emit('device_data', data)
        socketio.sleep(0.1)


if __name__ == '__main__':
    # 1. 启动MQTT订阅（连接公共Broker）
    start_mqtt_subscriber()
    # 2. 启动后台推送线程
    socketio.start_background_task(background_thread)
    # 3. 启动Web服务
    print("=" * 50)
    print("Web服务已启动: http://localhost:5000")
    print("再开一个终端运行模拟器:")
    print("python device/publisher_simulator.py")
    print("=" * 50)
    socketio.run(app, host='0.0.0.0', port=5000,
                 debug=False, allow_unsafe_werkzeug=True)
