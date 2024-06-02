# Favicon Adjustment Tools

## About
I created this project to provide a set of Python scripts designed to help with favicon customization and generation. The tools included in this project allow you to:

1. **Add Transparent Borders**: Enhance the appearance of favicon icons by adding transparent borders around them.
2. **Change Non-Transparent Pixel Colors**: Easily change the color of non-transparent pixels in PNG images, which is useful for quickly adjusting icon colors.
3. **Generate Basic Shapes**: Create basic shapes such as squares and triangles based on the properties of an input circle image, which can be used as favicons or other graphic elements.

These scripts utilize the Python Imaging Library (PIL) to perform image manipulations, making it simple to automate and customize favicon creation for various applications.

## Adding a Transparent Border
### `add-transparent-border.py`
This script adds a transparent border around an original input image, which is useful for displaying a favicon icon smaller on a browser tab.

<p align="center">
  <img src="media/examples/example1.png" alt="">
  <br>
  <em>Example of an icon shrunken using the add-transparent-border script</em>
</p>

#### Usage
1. Place your input image (e.g., `icon.png`) in the same directory as the script.
2. Set the desired border size in pixels (default is 200 pixels).
3. Run the script to generate the output image with the transparent border.


## Changing The Color of a PNG Favicon
### `change-non-transparent-pixels.py`
This script changes non-transparent pixels in a PNG image to a specified color.

<p align="center">
  <img src="media/examples/example2.png" alt="">
  <br>
  <em>Example of a recolored icon using the change-non-transparent-pixels script</em>
</p>

#### Usage
1. Place your input image (e.g., `icon3.png`) in the same directory as the script.
2. Set the desired color to change non-transparent pixels (default is red with some transparency).
3. Run the script to generate the output image with the new color.


## Basic Favicon Generation
### `generate-shapes.py`

## Basic Favicon Generation
### `generate-shapes.py`
This script generates square and triangle images based on an input circle image, using the circle's radius and color.

<p align="center">
  <img src="media/examples/example3.png" alt="">
  <br>
  <em>Example of generated favicons using the generate-shapes script</em>
</p>

#### Usage
1. Place your input circle image (e.g., `circle.png`) in the same directory as the script.
2. Run the script to generate square and triangle images based on the circle's properties.

