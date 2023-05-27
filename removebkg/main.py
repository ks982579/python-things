"""
Small script to (hopefully) remove background from images for Free!
"""

from PIL import Image
from rembg import remove
import easygui as eg

# Object to store path and name of file
input_path = eg.fileopenbox(title="Select Image File")

# Object to store path to save file
output_path = eg.filesavebox(title="Save File to...")

image_with_background = Image.open(input_path)
image_without_background = remove(image_with_background)

# Set format to PNG when saving
image_without_background.save(output_path)