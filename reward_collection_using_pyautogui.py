import pyautogui
import keyboard
import time  

# Define a termination function
def stop_loop():
    global keep_running
    keep_running = False
    print("Termination key pressed. Exiting loop...")

# Flag to control the loop
keep_running = True

def pc():
    # Mouse positions for each action
    positions = [(340, 155), (1315, 155), (1315, 667), (340, 667)]
    # Add hotkey to terminate the loop (e.g., when 'shift' is pressed)
    keyboard.add_hotkey('shift', stop_loop) 
    # Loop through ASCII values 65 (A) to 95 (^)
    for i in range(65, 95):
        char = chr(i)
        time.sleep(1)  # Delay before each iteration     
        for pos in positions:
            if not keep_running:
                break      
            pyautogui.moveTo(pos[0], pos[1], 1)
            pyautogui.click()
            pyautogui.press('backspace')
            pyautogui.write(char)
            pyautogui.press('enter')

def single_pc():
    keyboard.add_hotkey('shift', stop_loop) 
    for i in range(65, 95):
        char = chr(i) 
        time.sleep(6)
        if not keep_running:
            break  
        pyautogui.moveTo(340, 155)
        pyautogui.click()
        pyautogui.press('backspace')
        pyautogui.write(char)
        pyautogui.press('enter')
        
def mob():
    keyboard.add_hotkey('shift', stop_loop) 
    for i in range(65, 85):
        char = chr(i) 
        time.sleep(6)
        if not keep_running:
            break  
        pyautogui.moveTo(1550, 240)
        pyautogui.click()
        pyautogui.press('backspace')
        pyautogui.write(char)
        pyautogui.press('enter')

def minpc():  
    keyboard.add_hotkey('shift', stop_loop)   
    positions = [(820, 45), (1780, 34), (1784, 539), (808, 534)] 
    for pos in positions:
        if not keep_running:
            break
        pyautogui.moveTo(pos[0], pos[1], 1)
        pyautogui.click()

def chngmob(): 
    keyboard.add_hotkey('shift', stop_loop)  
    positions = [(348, 28), (1339, 933), (953, 590)]
    for pos in positions:
        if not keep_running:
            break
        pyautogui.moveTo(pos[0], pos[1], 1)
        pyautogui.click()
 
# for i in range(1, 4):
#     pc()
#     minpc()
# for i in range(1, 11):
#     mob()
#     chngmob()
    
for i in range(1, 5):
    mob()
    chngmob()

# pc()
# single_pc()
# mob()