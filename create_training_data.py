import numpy as np
from ScreenCapture.screen_capture import screen_capture
import cv2
import time
from KeyPress.check_keypress import get_pressed_key_list
from KeyPress.key_codes import get_key_vector
import os

starting_value = 1

while True:
    file_name = 'E:/code/TrackManiaAgent/data/training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        
        break

def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = screen_capture()
            screen = cv2.resize(screen, (240, 180))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            keys = get_pressed_key_list()
            output = get_key_vector(keys)
            training_data.append([screen,output])

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 500:
                    np.save(file_name,training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'E:/code/TrackManiaAgent/data/training_data-{}.npy'.format(starting_value)

                    
        keys = get_pressed_key_list()
        if ord('p') in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)

get_pressed_key_list()

main(file_name, starting_value)