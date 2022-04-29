from PIL import Image
from random import randint

fileDir = input("file location: ")
file = open(fileDir, "r")

width = 0
height = 0

img = ""

currentCol = ""
currentX = -1
currentY = 0

for line in file:
    if line.__contains__("width("):
        print("image width = " + line[6:])
        width = line[6:]
    if line.__contains__("height("):
        print("image height = " + line[7:])
        height = line[7:]
    if line.__contains__("setupDone"):
        img = Image.new(mode="RGB", size=(int(width), int(height)))
        pixels = img.load()
        print("image setup done")

    if line.__contains__("colour("):
        h = line[7:]
        currentCol = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        print("current colour now " + str(currentCol))
    if line.__contains__("line("):
        for i in range(int(line[5:])):
            if currentX < int(width) - 1:
                currentX += 1
            else:
                currentX = -1

            pixels[currentX, currentY] = currentCol
            print("pixel at " + str(currentX) + " " + str(currentY) + " changed")
    if line.__contains__("random("):
        red = randint(1, 254)
        green = randint(1, 254)
        blue = randint(1, 254)

        h = '%02x%02x%02x' % (red, green, blue)
        currentCol = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

        print("changed colour to random")
    if line.__contains__("down"):
        currentY += 1
        currentX = -1
        print("current y now " + str(currentY))

    if line.__contains__("binary("):
        binary = line[7:]

        if currentX < int(width) - 1:
            currentX += 1
        else:
            currentX = -1

        for char in binary:
            if char == "0":
                pixels[currentX, currentY] = (0, 0, 0)
                currentX += 1
            if char == "1":
                pixels[currentX, currentY] = (255, 255, 255)
                currentX += 1

    if line.__contains__("done"):
        img.save("out.png")

input("Press Enter to Exit...")
