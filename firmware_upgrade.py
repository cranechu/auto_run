#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cm
#
# Created:     22/08/2017
# Copyright:   (c) cm 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import subprocess
from aframework import *

def main():
    loop = 0
    while True:
        loop += 1
        print("loop %d\n" % loop)
        subprocess.Popen(["C:\\Users\\LITEON\\Desktop\\CL811T80_WIN.exe"])
        play_cut("firmware_upgrade")
        time.sleep(5)

if __name__ == '__main__':
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True
    main()
