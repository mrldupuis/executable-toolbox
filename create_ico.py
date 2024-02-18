from PIL import Image
filename = r'icons/exe_icon.png'
img = Image.open(filename)
img.save('icons/exe_icon.ico')