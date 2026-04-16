# CODE.PY
# COPYRIGHT 2026 JEONGWOO "RYAN" KIM KO6LVM

import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# 1. Setup LEDs as standard digital outputs
led7 = digitalio.DigitalInOut(board.GP7)
led7.direction = digitalio.Direction.OUTPUT

led8 = digitalio.DigitalInOut(board.GP8)
led8.direction = digitalio.Direction.OUTPUT

led9 = digitalio.DigitalInOut(board.GP9)
led9.direction = digitalio.Direction.OUTPUT

# Pin setup
# Value When Pressed is key reading when key is pressed,
# therefore False is when key is GROUNDed.
keyboard.matrix = KeysScanner(
    pins=[
        board.GP0, board.GP5, board.GP6,
        board.GP1, board.GP2, board.GP3, board.GP4
    ],
    value_when_pressed=False, 
)

# PTTLED 7 DCPTTLED 8 DCDEAFLED 9

# Keymap
keyboard.keymap = [
    [
        KC.F18, KC.F19, KC.F20,  # GP0, GP1, GP2 MX
        KC.F21,   KC.F22,   KC.F23, KC.F24 # GP3, GP4, GP5, GP6 On/Off
    ]
]


gp9_toggle_state = False
last_gp2_state = False

def led_logic(keyboard):
    global gp9_toggle_state, last_gp2_state

    # GP7 - GP0 Button - follows button status
    led7.value = keyboard.matrix.states[0]

    # GP8 - GP1 Button - follows button status
    led8.value = keyboard.matrix.states[1]

    # GP9 - GP2 Button - toggled
    current_gp2_state = keyboard.matrix.states[2]
    if current_gp2_state and not last_gp2_state:
        gp9_toggle_state = not gp9_toggle_state
    
    led9.value = gp9_toggle_state
    last_gp2_state = current_gp2_state

keyboard.before_matrix_scan.append(led_logic)

if __name__ == '__main__':
    keyboard.go()