import pyautogui
import keyboard

# Define a termination function
def key_pos():
    global keep_running
    keep_running = False

keep_running = True

# Add hotkey to terminate the loop (e.g., when 'shift' is pressed)
keyboard.add_hotkey('shift', key_pos)

while True:
    if not keep_running:
        print(pyautogui.position())
        keep_running = True