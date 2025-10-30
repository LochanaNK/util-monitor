import psutil
import time
from gpiozero import CPUTemperature

# import wmi

# w = wmi.WMI(namespace="root\\OpenHardwareMonitor")

# sensors = w.Sensor()
# for sensor in sensors:
#     if sensor.SensorType == u'Temperature':
#         print(sensor.Name, sensor.Value)


while True:
    cpu_usage = psutil.cpu_percent(interval = 1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    cpu = CPUTemperature()

    # temp_data = {k: v for k,v in temp_data.items()}
    # temp_value = ""
    # for sensor in temp_data.values():
    #     if(sensor['label'] == 'Core 0 Temperature'):
    #         temp_value = str(sensor['core']) + ": " + str(sensor['temp']) + "°C"
    #         break

    print(f"CPU: {cpu_usage}%, RAM: {memory.percent}%, Disk: {disk.percent}%, CPU Temp: {cpu.temperature}°C")
    time.sleep(2)