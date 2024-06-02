from PIL import Image, ImageDraw

def generate_square(circle_radius, circle_color):
    # Calculate the side length of the square using the circle's radius
    square_side = 2 * circle_radius
    # Create a new transparent square image
    square_img = Image.new('RGBA', (square_side, square_side), (0, 0, 0, 0))
    draw = ImageDraw.Draw(square_img)
    # Draw the square
    draw.rectangle((0, 0, square_side, square_side), fill=circle_color)
    return square_img

def generate_triangle(circle_radius, circle_color):
    # Calculate the side length of the equilateral triangle using the circle's radius
    triangle_side = 2 * circle_radius
    # Create a new transparent triangle image
    triangle_img = Image.new('RGBA', (triangle_side, triangle_side), (0, 0, 0, 0))
    draw = ImageDraw.Draw(triangle_img)
    # Calculate the coordinates of the triangle's vertices
    x1 = 0
    y1 = triangle_side
    x2 = triangle_side / 2
    y2 = 0
    x3 = triangle_side
    y3 = triangle_side
    # Draw the triangle
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=circle_color)
    return triangle_img

def main():
    # Open the circle image and get its properties
    circle_img = Image.open('circle.png')
    circle_width, circle_height = circle_img.size
    # Calculate the center coordinates of the circle
    center_x = circle_width // 2
    center_y = circle_height // 2
    # Get the color of the pixel at the center of the circle
    circle_color = circle_img.getpixel((center_x, center_y))
    # Calculate the radius of the circle
    circle_radius = min(circle_width, circle_height) // 2
    # Generate square and triangle images
    square_img = generate_square(circle_radius, circle_color)
    triangle_img = generate_triangle(circle_radius, circle_color)
    # Save the generated images
    square_img.save('square.png')
    triangle_img.save('triangle.png')
    print("Images generated successfully!")

if __name__ == "__main__":
    main()
