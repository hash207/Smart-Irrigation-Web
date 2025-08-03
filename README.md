# Smart Irrigation - Flask Web App

This is the backend web application for the Smart Irrigation System. It receives real-time soil moisture data via MQTT and visualizes it. The app is built with Flask and uses Socket.IO for live updates. Hosted using Ngrok or locally on a Raspberry Pi.

## Features

- Live soil moisture monitoring (via MQTT)
- Water valve control interface
- Ngrok integration for secure remote access
- Modular and Docker-compatible

## Setup

1. Clone this repo:  
   ```git clone https://github.com/yourusername/smart-irrigation-web.git```

2. Install dependencies:
   ```pip install -r requirements.txt```
3. Run the app:
   ```source run.sh```

## Deployment (Optional)

You can containerize this app using Docker or deploy it directly on a Raspberry Pi. Supports integration with MongoDB and n8n.
Live Access

This app is accessible at:
🌐 https://safe-shiner-daring.ngrok-free.app
