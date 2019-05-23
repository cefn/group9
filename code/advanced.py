# Set a random pixel to a random color every second
from vgkits.random import randint
clearPixels()
colors = [red, blue, green, yellow, purple, teal, white]
while 1 == 1:
    pixelPos = randint(8)
    colorPos = randint(len(colors))
    color = colors[colorPos]
    color = darkenRgb(color)
    setPixel(pixelPos, color)
    sleep(0.5)
