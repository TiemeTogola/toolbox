#!/usr/bin/env python

# TODO: setup python 3
#       see evdev docs
#       dependency injection?
#       integrate rxpy for async?

import statsd
import evdev #use the evdev event timestamp
from evdev import util
from evdev import ecodes

    # devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    # for device in devices:
        # print(device.fn, device.name, device.phys)


# temporary, statsd will do the insert
import sqlite3
client = sqlite3.connect('/home/tieme/workspace/test.sqlite')
def to_sqlite(metric):
    cursor = client.cursor()
    cursor.execute('INSERT INTO keypresses VALUES("1","press",' + str(metric) + ');')

def to_statsd(metric):
    print

def main():
    print(evdev.list_devices())
    print
    keyboard = evdev.InputDevice('/dev/input/event3')
    print(keyboard)
    print

    y = 0
    for event in keyboard.read_loop():
        if event.type != ecodes.EV_KEY: continue
        if event.value != 1: continue
        print(util.categorize(event))
        to_sqlite(y)    # just detect key press for now
        client.commit()
        y += 1
    client.close()

if __name__ == "__main__":
    main()
