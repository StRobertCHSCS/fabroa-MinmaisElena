from microbit import *
import radio
PIR_pin = pin0

radio.on()

while True:
    if PIR_pin.read_digital() == 1:
        radio.send("a message")
    else:
        radio.send("no")





