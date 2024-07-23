from PIL import Image
from image_converter import ListToImage, ImageToList


def main():
    # Open the image.
    dog_img = Image.open("dog.png")
    pixels = ImageToList(dog_img)

    # Apply the custom filter.
    filtered_pixels = apply_filter(pixels)

    # Save an image
    filtered_image = ListToImage(filtered_pixels)
    filtered_image.save("dog_filtered.png")
    return

def apply_filter(pixels):
    # Filter the image.
    new_pixels = []

    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            # The body of this loop merely makes a copy of pixels.
            r, g, b = pixels[row][col]
            middle = 225 / 2
            average = (r + g + b) / 3
            difference = average - middle

            r = middle - difference
            g = middle - difference
            b = middle - difference

            new_row.append((r, g, b))
        new_pixels.append(new_row)

    return new_pixels


main()