from PIL import Image

# adds transparent border around original input image
# used to display favicon icon smaller on browser tab

def add_transparent_border(input_image_path, output_image_path, border_size):
    # Open the input image
    image = Image.open(input_image_path)

    # Calculate new dimensions for the image with border
    new_width = image.width + 2 * border_size
    new_height = image.height + 2 * border_size

    # Create a new image with the calculated dimensions and transparent background
    new_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

    # Paste the original image onto the new image with an offset to account for the border
    new_image.paste(image, (border_size, border_size))

    # Save the result
    new_image.save(output_image_path)

# Example usage:
input_image_path = "icon.png"
output_image_path = "icon2.png"
border_size = 200  # Adjust this value to set the size of the border

add_transparent_border(input_image_path, output_image_path, border_size)