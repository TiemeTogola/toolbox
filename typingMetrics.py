#!/usr/bin/env python

# TODO: setup python 3
#       see evdev docs
#       integrate rxpy for async?

import statsd
import sqlite3
import evdev
from evdev import util
from evdev import ecodes

    # devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    # for device in devices:
        # print(device.fn, device.name, device.phys)

def to_sqlite(metric):
    print

def to_statsd(metric):
    print

def main():
    print(evdev.list_devices())
    print
    keyboard = evdev.InputDevice('/dev/input/event3')
    print(keyboard)
    print
    for event in keyboard.read_loop():
        print(util.categorize(event))

if __name__ == "__main__":
    main()
