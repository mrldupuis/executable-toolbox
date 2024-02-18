@echo off
call venv\Scripts\activate.bat
mkdir dist
python create_ico.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" animate_images.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" animate_images_recursive.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" pdf_compiler.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" pdf_compiler_recursive.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" pdf_interleaver.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" pdf_interleaver_recursive.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" image_to_pdf_converter.py
python -m PyInstaller -F --icon="icons//exe_icon.ico" image_to_pdf_converter_recursive.py

@echo on
del "*.spec"
echo y|rmdir /s build
pause