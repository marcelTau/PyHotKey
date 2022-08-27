import keyboard
import argparse
from time import sleep

keyboard_input = []

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--config', metavar='c', type=str, default='~/shortcut.cfg', help='path to config file.')
parser.add_argument('--sleep', metavar='s', type=float, default=0.1, help='sleep time waiting for keyboard input in seconds.')
parser.add_argument('--debug', metavar='d', type=bool, default=False, help='print debug output')
args = parser.parse_args()

goals = {}

with open(args.config) as file:
    content = file.readlines()
    for line in content:
        x = line.split('=')
        key = x[0]
        value = x[1]
        goals[key] = value

def simulate_keyboard(orig, text):
    for _ in orig:
        keyboard.press_and_release("backspace")
        sleep(0.01)
    keyboard.press_and_release("backspace")
        
    for c in text.strip():
        if c.isupper():
            keyboard.press('shift')
        keyboard.press_and_release(c.lower())
        if c.isupper():
            keyboard.release('shift')
        sleep(0.01)

while True:
    key = keyboard.read_key(True)
    keyboard_input.append(key)

    if len(keyboard_input) > 10:
        keyboard_input.pop(0)

    s = "".join(keyboard_input)

    if args.debug:
        print(s)

    for k, v in goals.items():
        if s.find(k + 'space') != -1:
            simulate_keyboard(k, v)
            keyboard_input.clear()

    sleep(args.sleep)
        
