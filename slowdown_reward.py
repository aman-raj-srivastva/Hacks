import pyautogui
import keyboard
import time  

def stop_loop():
    global keep_running
    keep_running = False
    print("Termination key pressed. Exiting loop...")

keep_running = True

def minpc():  
    keyboard.add_hotkey('shift', stop_loop)   
    positions = [(820, 45), (1780, 34), (1784, 539), (808, 534)] 
    for pos in positions:
        if not keep_running:
            break
        pyautogui.moveTo(pos[0], pos[1], 1)
        pyautogui.click()

def pc(n):
    positions = [(340, 155), (1315, 155), (1315, 667), (340, 667)]
    keyboard.add_hotkey('shift', stop_loop) 
    for i in range(n, n + 4):
        char = chr(i)
        time.sleep(1)   
        for pos in positions:
            if not keep_running:
                break      
            pyautogui.moveTo(pos[0], pos[1], 1)
            pyautogui.click()
            pyautogui.press('backspace')
            pyautogui.write(char)
            pyautogui.press('enter')
            
def mob(n):
    keyboard.add_hotkey('shift', stop_loop) 
    for i in range(n, n+4):
        char = chr(i) 
        time.sleep(6)
        if not keep_running:
            break
        pyautogui.moveTo(1550, 240)
        pyautogui.click()
        pyautogui.press('backspace')
        pyautogui.write(char)
        pyautogui.press('enter')
        
count = 0
internal_count = 0
while count < 7 and keep_running:
    time.sleep(900)
    pc(internal_count + 65)
    minpc()
    pc(internal_count + 65)
    pyautogui.moveTo(1521, 1053)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1461, 1053)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1401, 1053)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1346, 1053)
    pyautogui.click()
    count += 1 
    internal_count += 4

def mob_all(internal_count):
    count = 0
    while count < 6 and keep_running:
        mob(internal_count + 65)
        pyautogui.moveTo(343, 33)
        pyautogui.click()
        pyautogui.moveTo(871, 617)
        pyautogui.scroll(500)
        time.sleep(1)
        pyautogui.scroll(500)
        time.sleep(2)
        pyautogui.moveTo(933, 284)
        pyautogui.click()
        count += 1

count = 0
internal_count = 0  
while count < 4 and keep_running:
    time.sleep(860)
    mob_all(internal_count)
    count += 1
    internal_count += 4