from microbit import *


#  adapted from https://github.com/microbit-playground/microbit-servo-class 

import time


import radio
radio.on()


class Servo:

    """
    A simple class for controlling hobby servos.

    Args:
        pin (pin0 .. pin3): The pin where servo is connected.
        freq (int): The frequency of the signal, in hertz.
        min_us (int): The minimum signal length supported by the servo.
        max_us (int): The maximum signal length supported by the servo.
        angle (int): The angle between minimum and maximum positions.

    Usage:
        SG90 @ 3.3v servo connected to pin0
        = Servo(pin0).write_angle(90)
    """

    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        time.sleep(1)
        self.pin.write_digital(0)  # turn the pin off

    def write_angle(self, degrees=None):
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)


Servo_pin = pin2

servo = Servo(Servo_pin)

while True:
    new_message = radio.receive()
    if new_message == "a message":
        pin0.write_digital(1)  # turn pin0 (and the LED) on
        sleep(200)             # delay for half a second (500 milliseconds)
        pin0.write_digital(0)  # turn pin0 (and the LED) off
        sleep(200) 
        # pin1.write_digital(1)  # turn pin0 (and the LED) on
        # sleep(200)             # delay for half a second (500 milliseconds)
        # pin1.write_digital(0)  # turn pin0 (and the LED) off
        # sleep(500)      
        servo.write_angle(30) # changes servo position to 180
        time.sleep(1) # delays the next line of code by 1s
        servo.write_angle(0) # changes servo position back to 0
        time.sleep(1) # delays the next line of code by 1s
    else:
        pass