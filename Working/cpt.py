'''
-------------------------------------------------------------------------------
Name:		cpt.py
Purpose:	Detecting toxic chemicals in the soil

Author:	    Choi.H, Sedighi.R, Yu.Y

Created:	date in 21/01/2020
------------------------------------------------------------------------------
'''

from microbit import *
import music
import time
 
# defining pins
buzzer_pin = pin0
moisture_sensor_pin = pin1
led_pin = pin2
 
while True:
    if moisture_sensor_pin.read_analog() < 50:
        music.play('b3:1', pin = buzzer_pin)
        led_pin.write_digital(0)
        time.sleep(0.1)
        led_pin.write_digital(1)
        time.sleep(0.1)
    else:
        led_pin.write_digital(0)
