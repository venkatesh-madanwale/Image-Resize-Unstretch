---

# Image Resizer

This Python script resizes images in a specified folder to the dimensions of 768x1024 without visible stretching effect. It supports JPEG and PNG image formats.

## Installation

1. Clone this repository to your local machine:
   ```bash
   https://github.com/venkatesh-madanwale/Image-Resize-Unstretch.git
   ```

2. Navigate to the cloned repository:
   ```bash
   cd image-resizer
   ```

3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
## Results
![Input_Image](https://github.com/venkatesh-madanwale/urban-happiness/assets/71491587/fb48e019-b5ec-476c-a477-a3c78bf3a5da)
### Input [5412x7180]
![Output_Image](https://github.com/venkatesh-madanwale/urban-happiness/assets/71491587/209cc7d2-5aad-448f-89ba-4532b64c42a0)
### Output [768x1024]

## Usage

To resize images, follow these steps:

1. Place the images you want to resize in the `input_images` folder within the repository directory.
2. Run the script with the following command:
   ```bash
   python resize_images.py
   ```
3. The resized images will be saved in the `output_images` folder within the repository directory.

You can also specify custom input and output folders by modifying the `input_folder` and `output_folder` variables in the `resize_images.py` script.

```python
# Example usage:
input_folder = "custom_input_folder"
output_folder = "custom_output_folder"
resize_images(input_folder, output_folder)
```

## Example

Suppose you have a folder named `photos` containing images you want to resize. Follow these steps:

1. Place your images in the `photos` folder within the repository directory.
2. Modify the `input_folder` variable in the `resize_images.py` script:
   ```python
   input_folder = "photos"
   ```
3. Run the script as explained in the "Usage" section.
4. Resized images will be saved in the `output_images` folder within the repository directory.

---
