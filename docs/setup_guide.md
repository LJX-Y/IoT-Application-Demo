# 部署文档

## 环境要求

- Python 3.9+（Windows / Linux / macOS 均可）
- 可访问外网（连公共Broker和CDN）

## 安装步骤

```bash
# 1. 进入项目目录
cd IoT-Application-Demo

# 2. 创建虚拟环境（可选但推荐）
python -m venv venv
# Windows 激活:
venv\Scripts\activate
# Linux/Mac 激活:
source venv/bin/activate

# 3. 安装依赖（国内建议用清华镜像加速）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 4. 启动Web服务（终端1）
python backend/app.py

# 5. 启动数据模拟器（终端2）
python device/publisher_simulator.py

# 6. 浏览器打开
http://localhost:5000
```

## 生产环境改造方向

| 当前Demo | 生产环境 |
|---|---|
| 内存Queue | Redis / InfluxDB / TDengine |
| 公共Broker | 自建EMQX + 用户名密码认证 + TLS |
| Flask开发服务器 | Gunicorn + Nginx |
| 明文HTTP | HTTPS + 反向代理 |
| 单机 | Docker Compose 一键部署 |

## 常见问题

1. **页面白屏**：echarts/socket.io 走的CDN，需要联网
2. **收不到数据**：公共Broker偶尔不稳定，重启模拟器试试
3. **端口占用**：`netstat -ano | findstr 5000` 找到进程后结束，或改 app.py 里的端口
