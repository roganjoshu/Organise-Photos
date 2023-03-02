from PIL import Image

# Open the image
image = Image.open("C:\\Users\\joshu\\Pictures\\Screenshots\\Screenshot_20221122_205806.png")

# Convert the image to black and white
image = image.convert("1")

# Iterate over the pixels and print them to the console
for y in range(image.height):
    for x in range(image.width):
        pixel = image.getpixel((x, y))
        if pixel == 0:
            # Print a black pixel
            print("\u2588", end="")
        else:
            
            # Print a white pixel
            print(" ", end="")
    print()