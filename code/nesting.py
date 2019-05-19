def clearPixels():
    for pos in range(0, 8):
        setPixel(pos, black)

def fancyColors():
    pos = 0
    while pos < 8:
        for color in [green, blue, purple]:
            setPixel(pos, color)
            pos = pos + 1
            if pos < 8:
                continue
            else:
                break    

def colorSequence(colors, delay=1):
    for color in colors:
        for pos in range(0, 8):
            setPixel(color, pos)
            sleep(1) 
