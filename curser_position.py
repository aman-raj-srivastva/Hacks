import pyautogui
import keyboard

# Define a termination function
def key_pos():
    global keep_running
    keep_running = False
    
def terminate():
    global stop
    stop = True
    print("Termination key pressed. Program exited.")

keep_running = True
stop = False

# Add hotkey to terminate the loop (e.g., when 'shift' is pressed)
keyboard.add_hotkey('shift', key_pos)
keyboard.add_hotkey('alt', terminate)

while True:
    if not keep_running:
        print(pyautogui.position())
        keep_running = True
    elif stop:       
        break