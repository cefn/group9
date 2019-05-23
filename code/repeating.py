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
