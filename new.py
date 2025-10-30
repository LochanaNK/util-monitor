import time
import psutil
import clr

# Load OpenHardwareMonitor DLL
clr.AddReference(r'C:/Users/USER/Downloads/Compressed/openhardwaremonitor-v0.9.6/OpenHardwareMonitor/OpenHardwareMonitorLib')
from OpenHardwareMonitor.Hardware import Computer, SensorType, HardwareType

# Initialize Computer
pc = Computer()
pc.MainboardEnabled = True
pc.CPUEnabled = True
pc.Open()

def get_cpu_package_temp():
    for hw in pc.Hardware:
        if hw.HardwareType == HardwareType.CPU:
            hw.Update()
            # Look for package/core temp, ignore individual cores if possible
            for sensor in hw.Sensors:
                if sensor.SensorType == SensorType.Temperature:
                    # Filter out per-core temps if names include "Core"
                    if "Package" in sensor.Name or "CPU Package" in sensor.Name:
                        return sensor.Value
            # fallback: take first temperature if package not found
            for sensor in hw.Sensors:
                if sensor.SensorType == SensorType.Temperature:
                    return sensor.Value
    return None

while True:
    # CPU Usage (overall)
    cpu_percent = psutil.cpu_percent(interval=1)

    # Memory Usage
    mem = psutil.virtual_memory()
    mem_percent = mem.percent

    # CPU Package Temperature
    cpu_temp = get_cpu_package_temp()

    print(f"CPU Usage: {cpu_percent:.1f}%")
    print(f"CPU Temperature: {cpu_temp:.1f} °C" if cpu_temp else "CPU Temperature: N/A")
    print(f"Memory Usage: {mem_percent:.1f}% ({mem.used / 1024**2:.1f} MB / {mem.total / 1024**2:.1f} MB)")
    print("-" * 40)
    time.sleep(2)
