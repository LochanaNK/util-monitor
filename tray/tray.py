import time
import psutil
import clr
import json
import paho.mqtt.client as mqtt
import sys
import os
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

# ------------------ Load OpenHardwareMonitor DLL ------------------
if getattr(sys, 'frozen', False):
    exe_dir = sys._MEIPASS
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

dll_path = os.path.join(exe_dir, "OpenHardwareMonitorLib.dll")
clr.AddReference(dll_path)
from OpenHardwareMonitor.Hardware import Computer, SensorType, HardwareType

# ------------------ Initialize Hardware ------------------
pc = Computer()
pc.MainboardEnabled = True
pc.CPUEnabled = True
pc.Open()

# ------------------ MQTT Setup ------------------
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "home/pc/metrics"
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# ------------------ Monitoring Function ------------------
def get_cpu_package_temp():
    for hw in pc.Hardware:
        if hw.HardwareType == HardwareType.CPU:
            hw.Update()
            for sensor in hw.Sensors:
                if sensor.SensorType == SensorType.Temperature:
                    if "Package" in sensor.Name or "CPU Package" in sensor.Name:
                        return sensor.Value
            for sensor in hw.Sensors:
                if sensor.SensorType == SensorType.Temperature:
                    return sensor.Value
    return None

def monitor_loop():
    while True:
        cpu_percent = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory()
        cpu_temp = get_cpu_package_temp()

        data = {
            "cpu_usage": round(cpu_percent, 1),
            "cpu_temp": round(cpu_temp, 1) if cpu_temp else None,
            "memory_usage_percent": round(mem.percent, 1),
            "memory_used_MB": round(mem.used / 1024**2, 1),
            "memory_total_MB": round(mem.total / 1024**2, 1)
        }

        # Publish MQTT
        client.publish(MQTT_TOPIC, json.dumps(data))
        time.sleep(1)

# ------------------ Create System Tray Icon ------------------
def create_image():
    # Simple black square icon
    image = Image.new('RGB', (64, 64), color=(0, 0, 0))
    d = ImageDraw.Draw(image)
    d.text((10, 20), "PC", fill=(255, 255, 255))
    return image

def on_quit(icon, item):
    icon.stop()
    sys.exit(0)

menu = Menu(MenuItem('Quit', on_quit))
icon = Icon("PC Monitor", create_image(), menu=menu)

# Start monitoring in background thread
thread = threading.Thread(target=monitor_loop, daemon=True)
thread.start()

# Run the system tray icon
icon.run()
