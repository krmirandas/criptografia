fo = open("../imagen.enc", "rb")
image = fo.read()
fo.close()

image = bytearray(image)

for i in range(256):

    key = i

    for index, value in enumerate(image):
        image[index] = (value - key) % 256


    fo = open('./images/' + str(i) + ".jpg", "wb")

    fo.write(image)

fo.close()
