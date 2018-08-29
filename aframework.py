#!python

import os
import time
import datetime
import logging
import pyautogui

logging.basicConfig(level=logging.DEBUG)
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

"""
script: for one JQ test case, contains cuts
cut: for a serie of steps
step: trigger picture and target picture

target pciture contain the step operations
@ mouse
# keyboard
#..#.. hot key
$ parameter
% command: screen capture, end, ...
= split step name and step operations
"""

def operate_mouse(op):
    getattr(pyautogui, op)()

def operate_keyboard(op):
    if '#' not in op:
        pyautogui.typewrite(op)
    else:
        pyautogui.hotkey(*op.split('#'))

def operate_command(op):
    is_end = False
    if op == 'scapture':
        pyautogui.screenshot(datetime.datetime.now().strftime("%Y%m%d_%H%M%S.png"))
    elif op == 'end':
        is_end = True

    return is_end

def execute_operations(target, operations):
    is_end = False
    logging.info("target: %s", target)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(target, confidence=0.8))
    for op in operations:
        #print(op)
        logging.info("operation: %s", op)
        op_type = op[0]
        op = op[1:]
        if op_type == '@':
            operate_mouse(op)
        elif op_type == '#':
            operate_keyboard(op)
        elif op_type == '%':
            is_end = operate_command(op)

    return is_end

def check_trigger_images(cut, triggers):
    is_end = False
    for trig in triggers:
        #print(trig)
        if pyautogui.locateCenterOnScreen(trig, confidence=0.8):
            logging.info("get a trigger image: %s", trig)
            trig = os.path.basename(trig).split('.')[0]
            #print trig
            #print os.listdir(cut)
            #print [f for f in os.listdir(cut) if trig in f and "=" in f]
            for target_file in [f for f in os.listdir(cut) if trig in f and "=" in f]:
                operations = target_file.split("=")[1].split('.')[0]
                is_end_local = execute_operations(cut+"\\"+target_file, operations.split('_'))
                if is_end == False:
                    is_end = is_end_local

    return not is_end

#load all trigger and target pictures
#loop every 1 sec, to:
#  detect if trigger image occurs
#    locate mouse to the target position
#    parse the target operations
#      execute operation
def play_cut(cut_name):
    cut_path = "cuts\\" + cut_name
    files = [f for f in os.listdir(cut_path) if os.path.isfile(os.path.join(cut_path, f))]
    trigger_images = [cut_path+"\\"+f for f in files if '=' not in f]
    while check_trigger_images(cut_path, trigger_images):
        time.sleep(1)
    pyautogui.moveTo(pyautogui.size()[0]-1, pyautogui.size()[1]-1)

if __name__ == '__main__':
    #simple test with calc
    os.popen('calc')
    play_cut("calculate")
