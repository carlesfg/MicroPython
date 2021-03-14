# MicroPython
Micropython code to work with my students

This program allows you to measure the CO2 concentration in the air with the MH-Z19B sensor.
I have added two images with the connections between ESP32 and MH-Z19B, and between WeMos D1 ESP32 and MH-Z19B.
The Mhz19b class used in the program is a simplification of <a href="https://github.com/artem-smotrakov/esp32-weather-google-sheets">esp32-weather-google-sheets</a>.

Modify the line
SensorCO2 = Mhz19b (16, 17) # rx_pin = 16 and tx_pin = 17
to change the position of rx and tx 
