from PIL import Image

fileDir = input("file location: ")
file = Image.open(fileDir)
imgRGB = file.convert('RGB')
w, h = file.size
print(w, h)
out = open(fileDir + ".timg", "w")

out.write("width(" + str(w) + "\n")
out.write("height(" + str(h) + "\n")
out.write("setupDone\n\n")

for y in range(h):
    for x in range(w-1):
        colour = imgRGB.getpixel((x, y))
        h = '%02x%02x%02x' % colour
        out.write("colour(" + str(h) + "\n")
        out.write("line(1\n")
    out.write("down\n")

out.write("\n\ndone")