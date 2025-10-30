A tiny IoT project I built for fun to learn more about IoT and hardware monitoring. It runs a lightweight Python app on your PC that publishes system stats over MQTT to an ESP32, which shows the data on a small TFT display. Simple, local, and educational — perfect for learning networking, embedded systems, and system instrumentation.

🔧 How it works

  💠I package a Python script into a small executable that runs in the system tray on Windows.
  💠The script uses OpenHardwareMonitor and psutil to collect CPU usage, memory stats, and CPU temperature.
  💠It publishes the readings as JSON to a local Mosquitto MQTT broker running on the same network (localhost).
  💠An ESP32 connected to the same Wi-Fi subscribes to the MQTT topic, parses the JSON, and displays the stats on a TFT using an Arduino sketch.

⚠️ Current issues

  💠Windows Defender sometimes flags the generated Python .exe (and the OpenHardwareMonitor DLL) as suspicious. This is because bundlers and DLL loads look like packed/obfuscated binaries to heuristics.
  💠The app runs locally and needs a trusted build/signing to avoid false positives.
  💠MQTT messages can become noisy — some optimization of publish frequency and payload structure would help reduce clutter.

✨ Planned improvements

  💠Fix Defender warnings
    • Produce a cleaner PyInstaller build, add metadata, and (ideally) sign the binary with a code-signing certificate.
  💠Harden the hardware DLL handling
    • Ship the DLL responsibly, document it, and avoid suspicious packing/compression.
  💠Optimize MQTT
    • Tune publish frequency, use compact payloads, and add QoS/topic structure to avoid clutter.
  💠More utilities & analytics
    • Add more sensors, compute rolling averages, and provide suggestions (e.g., "CPU high — check background processes").
  💠Visualization & history
    • Add small graphs on the ESP32 or a separate script/server that stores and graphs historical data.

🧩 Tech stack

  💠Python (psutil, pystray, paho-mqtt, pythonnet/CLR for OpenHardwareMonitor)
  💠OpenHardwareMonitorLib.dll for Windows sensor data
  💠Mosquitto (local) as MQTT broker
  💠ESP32 + TFT display (Arduino sketch) to render the dashboard
