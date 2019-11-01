'''

-------------------------------------------------------------------------------

Name:       step_counter.py

Purpose:    To count steps using microbit

 

Author: choi.E

 

Created:    24/10/2019

------------------------------------------------------------------------------

'''
from microbit import *
import music

count = 0
direction = 'North'
Buzzer_pin = pin0
LED_pin = pin1


def display_count():
    display.scroll(str(count))


def increment_count():
    global count
    count += 1


def get_heading():
    global LED_pin
    angle = compass.heading()
    if (angle == 0):
        direction = 'North'
    elif (angle > 0 and angle < 90):
        direction = 'Northeast'
    elif (angle == 90):
        direction = 'East'
    elif (angle > 90 and angle < 180):
        direction = 'Southeast'
    elif (angle == 180):
        direction = 'South'
    else:
        direction = 'Northwest'
    LED_pin.write_digital(1)
    display.scroll(str(direction))
    LED_pin.write_digital(0)


def reset_count():
    count = 0
    music.play('f3:1', pin=Buzzer_pin)
    display.scroll(int(count))
    main()


def button_clicks():
    if button_a.is_pressed():
        reset_count()
    elif button_b.is_pressed():
        get_heading()
        main()


def main():
    while(True):
        display_count()
        if accelerometer.was_gesture('shake'):
            increment_count()
        button_clicks()    


main()
Buzzer_pin = "global"