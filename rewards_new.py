import pyautogui
import keyboard
import time
from random_word import RandomWords

r = RandomWords()

# Define a termination function
def stop_loop():
    global keep_running
    keep_running = False
    print("Termination key pressed. Exiting loop...")

# Flag to control the loop
keep_running = True

def pc():
    positions = [(340, 180), (1315, 180), (1315, 690), (340, 690)]
    keyboard.add_hotkey('shift', stop_loop)

    for _ in range(20):
        if not keep_running:
            break
        time.sleep(1)

        for pos in positions:
            if not keep_running:
                break
            pyautogui.moveTo(pos[0], pos[1], 1)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "a")   
            pyautogui.press("backspace")    
            pyautogui.write(r.get_random_word())
            pyautogui.press("enter")

def single_pc():
    keyboard.add_hotkey('shift', stop_loop) 
    for _ in range(20):
        if not keep_running:
            break
        time.sleep(6)
        pyautogui.moveTo(340, 155)
        pyautogui.click()
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace")
        pyautogui.write(r.get_random_word())
        pyautogui.press("enter")
        
def minpc():  
    keyboard.add_hotkey('shift', stop_loop)   
    positions = [(820, 45), (1780, 34), (1784, 539), (808, 534)] 
    for pos in positions:
        if not keep_running:
            break
        pyautogui.moveTo(pos[0], pos[1], 1)
        pyautogui.click()

# Main execution
def main():
    for i in range(1, 5):
        pc()
        minpc()
    single_pc()
    
main()
