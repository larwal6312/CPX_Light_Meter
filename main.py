import time
from adafruit_circuitplayground.express import cpx

red = (90, 0, 0)
off = (0, 0, 0)
cpx.pixels.brightness = 0.3
cpx.pixels.auto_write = True
last_level = 0

def levels():
    level = cpx.light
    print("level is %s" %(level))
    return level

def pixel_numbers(level):
    if level <= 10:
        pixel_range = 1
    elif 11 <= level <= 20:
        pixel_range = 2
    elif 21 <= level <= 30:
        pixel_range = 3
    elif 31 <= level <= 40:
        pixel_range = 4
    elif 41 <= level <= 50:
        pixel_range = 5
    elif 51 <= level <= 60:
        pixel_range = 6
    elif 61 <= level <= 70:
        pixel_range = 7
    elif 71 <= level <= 80:
        pixel_range = 8
    elif 81 <= level <= 90:
        pixel_range = 9
    elif level > 90:
        pixel_range = 10
    return pixel_range

while True:
    if cpx.switch:
        level = levels()
        pixel_range = pixel_numbers(level)

        if level >= last_level:
            for number in range(pixel_range):
                cpx.pixels[number] = red
                time.sleep(.05)
            last_level = level
        elif level < last_level:
            for number in reversed(range(pixel_range,10)):
                cpx.pixels[number] = off
                time.sleep(.05)
            last_level = level

        time.sleep(.05)
    elif not cpx.switch:
        cpx.pixels.fill((off))
