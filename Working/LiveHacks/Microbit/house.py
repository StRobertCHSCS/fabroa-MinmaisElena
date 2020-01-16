from microbit import *
import time

# pins
LED_PINr = pin0
LED_PINg = pin1
LED_PINb = pin2


while True:
    LED_PINr.write_digital(1) # turns on LED
    time.sleep(0.25) # delays the next line of code for 0.5s
    LED_PINr.write_digital(0) # turns off LED
    time.sleep(0.25) # delays the next line of code for 0.5s

    LED_PINg.write_digital(1) # turns on LED
    time.sleep(0.25) # delays the next line of code for 0.5s
    LED_PINg.write_digital(0) # turns off LED
    time.sleep(0.25) # delays the next line of code for 0.5s


    LED_PINb.write_digital(1) # turns on LED
    time.sleep(0.25) # delays the next line of code for 0.5s
    LED_PINb.write_digital(0) # turns off LED
    time.sleep(0.25) # delays the next line of code for 0.5s