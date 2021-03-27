import win32api as wapi
import time

keyList = [0x26, 0x28, 0x25, 0x27, ord('p')]

def get_pressed_key_list():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(key):
            keys.append(key)
    return keys