import PIL.Image
from PIL import ImageOps

# Set the ASCII characters used for rendering
ASCII_CHARS = '@%#*+=-:. '

def convert_to_ascii(image_path):
    # Open the image file using Pillow
    img = PIL.Image.open(image_path)

    # Convert the image to grayscale
    img = img.convert('L')

    # Resize the image (optional)
    # img = img.resize((100, 100))  # Example: resize to 100x100 pixels

    # Get the dimensions of the original image
    width, height = img.size

    # Initialize the ASCII art string
    ascii_art = ''

    # Iterate over each pixel in the grayscale image
    for y in range(height):
        for x in range(width):
            # Get the grayscale value (0-255) for this pixel
            gray_value = img.getpixel((x, y))

            # Map the grayscale value to an ASCII character
            ascii_char = ASCII_CHARS[gray_value * len(ASCII_CHARS) // 256]

            # Add the ASCII character to the ASCII art string
            ascii_art += ascii_char

        # End of row
        ascii_art += '\n'

    return ascii_art

def save_to_file(ascii_art, file_path):
    with open(file_path, 'w') as file:
        file.write(ascii_art)

# Example usage:
image_path = '/Users/mac/PycharmProjects/pythonProject/IMG_0197.jpg'  # Update this path
ascii_art = convert_to_ascii(image_path)

# Save the ASCII art to a text file
file_path = '/Users/mac/PycharmProjects/pythonProject/ascii_art.txt'  # Update this path
save_to_file(ascii_art, file_path)

print(f"ASCII art saved to {file_path}")
