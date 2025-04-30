# Smart Irrigation System

An IoT-based smart irrigation system built using:

- **Arduino Uno + NodeMCU (ESP8266)** for reading soil moisture sensors and sending data
- **Raspberry Pi 4** running a **Flask web server** to monitor and log sensor readings
- **MQTT protocol** for efficient communication between devices
- **Ngrok** to expose the Flask web app to the internet

---

## 🌱 Project Goal

Automatically monitor and control garden irrigation based on real-time soil moisture data.  
The system improves water efficiency and gives users remote access via a live dashboard.

---

## 🔧 Hardware Components

- Arduino Uno (reading analog sensor data)
- NodeMCU ESP8266 (for WiFi + MQTT publishing)
- Soil moisture sensors
- Relay module (to control water valves)
- Raspberry Pi 4 (MQTT broker + web server)
- Optional: LDR sensor for simulation/testing

---

## ⚙️ Software Stack

| Component | Technology |
|----------|------------|
| Backend | Python + Flask |
| Communication | MQTT via Eclipse Paho |
| Broker | Mosquitto (can be local or hosted) |
| Web Interface | Flask + HTML |
| Deployment | Docker (optional) |
| Tunneling | Ngrok (Free Static URL) |

---

## 🌐 Live Access

The web dashboard is publicly accessible via:
**[https://starfish-regular-lightly.ngrok-free.app](https://starfish-regular-lightly.ngrok-free.app)**

(Note: Ngrok free static IPs may sleep when idle.)

---

## 📡 Communication Logic

- NodeMCU reads moisture values and compares them to the last value.
- If the change exceeds the threshold (e.g., 10%), it sends data to the MQTT broker.
- Flask web app subscribes to the topic and updates the web interface in real-time.

---

## 🐳 Docker Support

To containerize the web server:

```bash
docker build -t smart-irrigation .
docker run -d -p 5000:5000 smart-irrigation