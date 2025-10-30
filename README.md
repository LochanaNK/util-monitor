This is a small IoT project I did for fun and to learn more about IoT, which is a PC resource monitor.

How it works,

  I created a Python exe file to run in the system tray to get the resource data and publish them to the ESP-32.
  I used Eclipse Mosquitto MQTT for this and it runs only locally.
  Then, using the ESP-32 Wi-Fi, I connect to the same Wi-Fi as the PC connected to.
  Using MQTT, the data will be received as JSON objects, and the Arduino sketch will read them and display them on a small TFT display.
  I used OpenHardWareMonitor library to get the pc resource data.

Issues with this setup,

  The Python exe file is not created to meet the security requirements of Windows Defender since I do not have knowledge of that yet, so it might be considered as a threat.
  The hardware library I used is somehow considered a threat by Windows Defender  as well.

Future Improvements,

  Fixing all the issues mentioned above.
  Adding more utilities to monitor and display.
  Optimizing the Mosquitto publishing and subscription so data would not get cluttered.
  And hopefully add graphs and a separate scripts to monitor and calculate avg values and suggestions to improve based on the calculations.
