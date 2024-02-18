import os
from pathlib import Path
import fitz

def chkList(lst):
    return len(set(lst)) == 1

file_list = list(Path(os.getcwd()).glob('*.pdf'))
if len(file_list)>0:
	docs = [fitz.open(f) for f in file_list]
	lengths = [d.page_count for d in docs]

	if not chkList(lengths):
		print(f'Program can only interleave pdfs with matching lengths; currently lengths are :{lengths}')
		input("Press enter to close...")

	merger = fitz.open()
	for p in range(0,lengths[0]):
		for doc in docs:
			merger.insert_pdf(doc,to_page=p,from_page=p)

	merger.save("pdf_interleaver.pdf")

