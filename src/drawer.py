import time
import autoit
import keyboard
import pyperclip
from load_picture import load_picture


def start_draw():
    pixels = load_picture()
    min_x, max_x = 634, 1285
    min_y, max_y = 154, 804
    prev_hex = None

    time.sleep(5)
    for y in range(32):
        for x in range(32):
            if keyboard.is_pressed("F5"):
                exit()
            r, g, b = pixels[x, y]
            hex_color = f"#{r:02X}{g:02X}{b:02X}"
            if prev_hex != hex_color:
                autoit.mouse_click("left", 1093, 859, speed=2)
                autoit.mouse_click("left", 1089, 758, speed=2)
                pyperclip.copy(hex_color)
                autoit.send("^v")
                time.sleep(0.1)
                autoit.send("{ENTER}")
                autoit.mouse_click("left", 1344, 470, speed=2)
            prev_hex = hex_color
            pixel_width = (max_x - min_x) / 32
            pixel_height = (max_y - min_y) / 32
            screen_x = min_x + x * pixel_width + pixel_width / 2
            screen_y = min_y + y * pixel_height + pixel_height / 2
            autoit.mouse_click("left", int(screen_x), int(screen_y), speed=2)
    return True