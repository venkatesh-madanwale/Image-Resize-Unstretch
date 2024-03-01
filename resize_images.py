import os
from PIL import Image

def resize_images(input_folder, output_folder, width=768, height=1024):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of files in input folder
    files = os.listdir(input_folder)
    
    # Iterate through each file
    for file_name in files:
        input_path = os.path.join(input_folder, file_name)
        
        # Check if file is an image (jpg or png)
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Open image
            image = Image.open(input_path)
            
            # Resize image without visible stretching effect
            resized_image = image.resize((width, height), Image.LANCZOS)
            
            # Save resized image
            output_path = os.path.join(output_folder, file_name)
            resized_image.save(output_path)
            print(f"Resized {file_name} and saved as {output_path}")

# Example usage:
input_folder = "input_images"
output_folder = "output_images"
resize_images(input_folder, output_folder)
