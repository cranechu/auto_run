# auto_run
Based on pyautogui, automatically do something on GUI. It is tested in Windows 10. 
You do not need to write any line of code. Some screenshots, as well as actions in filenames, are enough. 

Usage:
1. install python 3.7
2. pip install pyautogui
3. pip install opencv-python
4. prepare target and action pictures in "cuts" folder
5. use action filename as the actions:
```
   - @ mouse
   - # keyboard
   - #..#.. hot key
   - $ parameter
   - % command: screen capture, end, ...
   - = split step name and step operations
```

Find more information on pyautogui: https://pyautogui.readthedocs.io/en/latest/
