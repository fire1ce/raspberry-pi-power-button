#!/usr/bin/python3
from datetime import datetime, timedelta
from time import sleep
from signal import pause
from gpiozero import Button
import os

use_button = 3  # pin 5
held_for = 0.0
Button.pressed_time = None


def released():
    global held_for
    if (held_for > 3.0):
        print("Shuting down...")
        os.system("shutdown now -h")
    else:
        held_for = 0.0


def pressed(button):
    if button.pressed_time:
        if button.pressed_time + timedelta(seconds=1) > datetime.now():
            print("rebooting...")
            os.system("reboot")
        button.pressed_time = None
    else:
        # print("pressed once")  # debug
        button.pressed_time = datetime.now()


def held():
    global held_for
    held_for = max(held_for, button.held_time + button.hold_time)


button = Button(use_button, hold_time=1.0, hold_repeat=True)
button.when_held = held
button.when_released = released
button.when_pressed = pressed

pause()
