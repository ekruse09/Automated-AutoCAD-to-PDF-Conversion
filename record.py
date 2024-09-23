import pyautogui

# Continuously print the mouse coordinates
print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and display the mouse coordinates
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)  # Erase the previous position output
except KeyboardInterrupt:
    print('\nDone.')