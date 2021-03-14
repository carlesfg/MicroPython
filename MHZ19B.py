# This class measures CO2 with the MH-Z19B sensor on ESP32 or WeMos D1 R32
class Mhz19b:

    # initializes a new instance
    def __init__(self,rx_pin, tx_pin):
        self.uart = UART(1, baudrate=9600, bits=8, parity=None, stop=1, rx=int(rx_pin) ,tx=int(tx_pin))
        

    # measure CO2
    def measure(self):
        while True:
            # send a read command to the sensor
            self.uart.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')

            # a little delay to let the sensor measure CO2 and send the data back
            time.sleep(1)  # in seconds

            # read and validate the data
            buf = self.uart.read(9)
            if self.is_valid(buf):
                break

            # retry if the data is wrong  
            print('error while reading MH-Z19B sensor: invalid data')
            print('retry ...')


        # make this operation
        co2 = buf[2] * 256 + buf[3]
        return [co2]

    # check data returned by the sensor 
    def is_valid(self, buf):
        if buf is None or buf[0] != 0xFF or buf[1] != 0x86:
            return False
        i = 1
        checksum = 0x00
        while i < 8:
            checksum += buf[i] % 256
            i += 1
        checksum = ~checksum & 0xFF
        checksum += 1
        return checksum == buf[8]

# Here begins the program 
import machine
import time
from machine import Pin 
from machine import UART
from time import sleep_ms

SensorCO2 = Mhz19b(16, 17) # rx_pin= 16 and tx_pin= 17

for x in range(1, 50): # We take 50 measurements 
    print("Iteration = " , x) # Iteration x
    # we add the list of 1 member and convert it to "int" number 
    reading = int(sum(SensorCO2.measure())) 
    print("Reading =", reading)
    print(" ") #  Blank space 
    sleep_ms(500)
