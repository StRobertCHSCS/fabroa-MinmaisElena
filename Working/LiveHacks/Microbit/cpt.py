from microbit import *
import music
import time
Buzzer_pin = pin0
MoistureSensor_pin = pin1
LED_pin = pin2
while True:
    if MoistureSensor_pin.read_analog() < 50:
        music.play('b3:1', pin=Buzzer_pin)
        LED_pin.write_digital(0)
        time.sleep(0.1)
        LED_pin.write_digital(1)
        time.sleep(0.1)
    else:
        LED_pin.write_digital(0)