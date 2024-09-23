import os
import subprocess
import time
import pyautogui

pyautogui.FAILSAFE = False

# Path to Autocad LT executable
autocad_exe = r"C:\Program Files\Autodesk\AutoCAD LT 2025\acadlt"

# Folder containing DWG files
dwg_folder = r"C:\Users\jschr\Downloads\OneDrive\Documents\Work\Given Documents\CAD Drawings"

# List all DWG files in the folder
dwg_files = [file for file in os.listdir(dwg_folder) if file.endswith('.dwg')]


actions = [
    {'type': 'mouse_click', 'x': 3323, 'y': 1002, 'button': 'left'},
    {'type': 'keystroke', 'key': '.'},
    {'type': 'keystroke', 'key': 's'},
    {'type': 'keystroke', 'key': 'c'},
    {'type': 'keystroke', 'key': 'r'},
    {'type': 'keystroke', 'key': 'i'},
    {'type': 'keystroke', 'key': 'p'},
    {'type': 'keystroke', 'key': 't'},
    {'type': 'keystroke', 'key': 'enter'},
    {'type': 'mouse_click', 'x': 3005, 'y': 322, 'button': 'left'},
    {'type': 'open_file', 'x': 3634, 'y': 326, 'button': 'left'},
    {'type': 'final_mouse_click', 'x': 1889, 'y': 11, 'button': 'left'}
]

def perform_actions(actions):
    for action in actions:
        if action['type'] == 'keystroke':
            if action['key'] == 'enter':
                pyautogui.press('enter')
            else:
                pyautogui.typewrite(action['key'], interval=0.1)  # Adjust interval as needed
        elif action['type'] == 'mouse_move':
            pyautogui.moveTo(action['x'], action['y'], duration=0.2)  # Adjust duration as needed
        elif action['type'] == 'mouse_click':
            pyautogui.click(action['x'], action['y'], button=action['button'], duration=0.1)  # Adjust duration as needed
        elif action['type'] == 'final_mouse_click':
            time.sleep(5)
            pyautogui.click(action['x'], action['y'], button=action['button'], duration=0.1)
        elif action['type'] == 'open_file':
            pyautogui.click(action['x'], action['y'], button=action['button'], duration=0.1)
            time.sleep(0.1)
            pyautogui.click(action['x'], action['y'], button=action['button'], duration=0.1)

        time.sleep(1)  # Adjust sleep time between actions if necessary


# Loop through each DWG file and process
for dwg_file in dwg_files:
    dwg_path = os.path.join(dwg_folder, dwg_file)
    
    # Command to run Autocad LT
    open_cad = [autocad_exe, dwg_path]  
    
    try:
        # Start AutoCAD LT
        subprocess.Popen(open_cad)
        
        print(f"AutoCAD LT started. Processing {dwg_file}...")
        
        # Wait for AutoCAD to open and load the DWG file (adjust sleep time if necessary)
        time.sleep(20)  # Adjust as needed based on how long AutoCAD takes to open
        
        print("Starting actions. HANDS OFF MOUSE AND KEYBOARD")

        perform_actions(actions)
        
        print(f"Script executed successfully for {dwg_file}.")
        
        
    except subprocess.CalledProcessError as e:
        print(f"Error processing {dwg_file}: {e}")
        
    except Exception as e:
        print(f"Error: {e}")
    
