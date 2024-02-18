import os
from pathlib import Path
import img2pdf
from PIL import Image

file_list = []
for extension in ['*.tif','*.tiff','*.png','*.jpg','*.jpeg']:
	file_list.extend(Path(os.getcwd()).rglob(extension))
	file_list.extend(Path(os.getcwd()).rglob(extension.capitalize()))

for f in file_list:
	# opening image
	image = Image.open(f)
	
	# converting into chunks using img2pdf
	pdf_bytes = img2pdf.convert(image.filename)

	# opening or creating pdf file
	myfile = open(f.with_suffix('.pdf'),'wb')

	# writing pdf files with chunks
	myfile.write(pdf_bytes)

	# closing image file
	image.close()
	
	# closing pdf file
	myfile.close()
	
	# output
	print(f"Successfully made {myfile}")