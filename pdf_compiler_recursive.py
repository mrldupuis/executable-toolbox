import os
from pathlib import Path
import fitz

merger = fitz.open()
for my_file in Path(os.getcwd()).rglob('*.pdf'):
	with fitz.open(my_file) as mfile:
		merger.insert_pdf(mfile)
merger.save("pdf_compiler_recursive.pdf")
