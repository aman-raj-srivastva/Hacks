import pyautogui
import keyboard
import time  

# Flag to control the loop
keep_running = True

# Define a termination function
def stop_loop():
    global keep_running
    keep_running = False
    print("Termination key pressed. Exiting loop...")

# Add hotkey to terminate the loop (e.g., when 'shift' is pressed)
keyboard.add_hotkey('shift', stop_loop)

# Mouse positions for each action
# positions = [(340, 155), (1315, 155), (1315, 667), (340, 667)]
positions = [(340, 155)] 
# positions = [(340, 198)] 

# Loop through ASCII values 65 (A) to 83 (S)
for i in range(65, 94):
    char = chr(i)

    time.sleep(6)  # Delay before each iteration
    # time.sleep(1)  # Delay before each iteration
    
    # Iterate through predefined positions
    for pos in positions:
        
        if not keep_running:
            break  # Break the loop if the stop signal is triggered
        
        pyautogui.moveTo(pos[0], pos[1], 1)
        pyautogui.click()
        pyautogui.press('backspace')
        pyautogui.write(char)
        pyautogui.press('enter')


# Optional: Clean up by unbinding the hotkey after the loop ends
keyboard.remove_hotkey('shift')