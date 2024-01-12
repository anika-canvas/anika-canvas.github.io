from PIL import Image
import os

# Global variable for the target size
TARGET_SIZE = 1000

def scale_image(input_path, output_path, max_size):
    original_image = Image.open(input_path)
    
    # Get original width and height
    original_width, original_height = original_image.size
    
    # Calculate new width and height while maintaining the aspect ratio
    if original_width > original_height:
        new_width = max_size
        new_height = int((max_size / original_width) * original_height)
    else:
        new_height = max_size
        new_width = int((max_size / original_height) * original_width)
    
    # Resize the image
    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    
    # Save the resized image
    resized_image.save(output_path)

def process_images(directory_path):
    # Ensure the directory path ends with a '/'
    directory_path = directory_path.rstrip('/') + '/'
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Construct the full path for the image
            image_path = os.path.join(directory_path, filename)
            
            # Get image dimensions
            with Image.open(image_path) as img:
                width, height = img.size
            
            # Check if either width or height is greater than the target size
            if width > TARGET_SIZE or height > TARGET_SIZE:
                # Scale the image and replace the original
                scale_image(image_path, image_path, TARGET_SIZE)
                print(f"Resized {filename} to {TARGET_SIZE}x{TARGET_SIZE}")

# Replace '/gallery' with the path to your image directory
process_images('website Images')

