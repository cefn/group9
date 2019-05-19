intro = "Why was 6 afraid of 7?"
numbers = list(range(7, 10))
punchline = "Because " + str(numbers)
print(punchline)

def tellJoke():
    print("Why was 6 afraid of 7?")
    numbers = list(range(7, 10))
    print("Because " + str(numbers))
    
tellJoke()


def setAll(color):
    for pos in range(0, 8):
        setPixel(pos, color)

setAll(blue)
