import os
from pathlib import Path
import imageio

duration = input("Enter seconds per frame: ")
file_list = []
for extension in ['*.tif','*.tiff','*.png','*.jpg','*.jpeg']:
	file_list.extend(Path(os.getcwd()).rglob(extension))
	file_list.extend(Path(os.getcwd()).rglob(extension.capitalize()))
file_list = sorted(file_list)

images = []
for filename in file_list:
	images.append(imageio.imread(filename))
imageio.mimsave(os.path.join(os.getcwd(),'animate_images_recursive.gif'), images, duration=duration)
