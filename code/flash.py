# Alternate Red with Blue every second
clearPixels()
while 1 == 1:
    setPixel(0, red)
    sleep(1)
    setPixel(0, blue)
    sleep(1)


# Move a single red pixel along the display
while 1 == 1:
    for pos in range(0, 8):
        clearPixels()
        setPixel(pos, red)
        sleep(1)

        
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
