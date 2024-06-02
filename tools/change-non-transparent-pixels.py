from PIL import Image

#   Change non-transparent pixels in a PNG image to the specified color.
#   image_path: path to the input PNG image.
#   output_path: path to save the output image.
#   color: tuple representing the RGB color to change non-transparent pixels to.

def change_non_transparent_pixels(image_path, output_path, color):
    # Open the image
    img = Image.open(image_path)
    # Convert image to RGBA if it's not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    # Get pixel data
    pixels = img.load()
    width, height = img.size
    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Check if the pixel is not transparent
            if pixels[x, y][3] != 0:
                # Change the pixel color to the specified color
                pixels[x, y] = color
    # Save the modified image
    img.save(output_path)

def main():
    input_image_path = "icon3.png"
    output_image_path = "icon4.png"
    color_to_set = (255, 0, 0, 100)  # Red color
    change_non_transparent_pixels(input_image_path, output_image_path, color_to_set)
    print("Images generated successfully!")

if __name__ == "__main__":
    main()