# 🦾 EMG Fitness Armband — Real-Time Muscle Monitoring System

A wearable EMG (electromyography) armband that streams live muscle data wirelessly to a real-time web dashboard. Built for a client (Mark) with limited hand dexterity as an accessibility-focused engineering project at McMaster University.

## 📊 Key Metrics

| Metric | Result |
|---|---|
| 🎯 Accuracy | 95% success rate (final trials) |
| 🪶 Weight | 68.8g (target: <120g) |
| ⚡ Latency | <0.5 seconds (real-time feedback) |
| 🙌 User Independence | 100% success rate putting it on/off |

## 🧠 How It Works

1. **Hardware** — Dry MyoWare EMG sensors inside a washable fabric sleeve detect electrical muscle signals
2. **ESP32** — Microcontroller reads sensor data and hosts a local HTTP endpoint over Wi-Fi
3. **bridge.py** — Python WebSocket bridge fetches data from the ESP32 (`/sensor`) and streams it to the browser at <0.5s latency
4. **Dashboard** — HTML/CSS/JS frontend (`mark.html`, `mark.js`, `chart.js`) renders live muscle activity charts with high-contrast visuals for accessibility

## 🗂️ File Structure
```
bridge.py               # Python WebSocket server — bridges ESP32 → browser
bridge_without_wifi.py  # USB/serial fallback version
mark.html               # Main dashboard UI
mark.css                # High-contrast styling for accessibility
mark.js                 # WebSocket client + real-time chart updates
chart.js                # Chart rendering logic
mark_2charts.js         # Dual-arm tracking version
```

## 🛠️ Tech Stack

- **Hardware:** ESP32 (Wi-Fi/BLE), MyoWare EMG dry sensors, fabric sleeve + Velcro
- **Backend:** Python, WebSockets, PySerial, asyncio
- **Frontend:** Vanilla JavaScript, HTML5, CSS3, Chart.js
- **Firmware:** C++/Arduino (ESP32 signal processing)

## 🚀 Running the Dashboard

1. Connect ESP32 to same Wi-Fi network
2. Run the bridge: `python bridge.py`
3. Open `mark.html` in your browser
4. Start moving — muscle data streams live to the chart

## 👥 Team — Mon-35 (McMaster University, Jan–Apr 2025)

- **Ronn Philip** — Software lead (Python backend, WebSocket pipeline, dashboard UI)
- Julia Leszczynski — Hardware & prototype fabrication
- Zoeya Parrey — UI design & medical research
- Xinrui Wu — C++/Arduino firmware & frontend
chart.js               # Chart rendering logic
mark_2charts.js        # Dual-arm tracking version
