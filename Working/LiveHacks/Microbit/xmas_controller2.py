from microbit import *
import radio 
radio.on()
while True:
    new_message = radio.receive()
    if new_message == "a message":
        display.scroll("snake")
    else:
        display.scroll("--")
