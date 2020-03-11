# utility tool to split or merge pdf files
# code heavily borrowed from:
# https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
# https://stackoverflow.com/questions/3444645/merge-pdf-files

from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from tkinter import Tk
from tkinter import filedialog
import pyautogui
import os

def get_filenames():
    width, height = pyautogui.size()
    geometry_str = f'1x1+{int(width/5)}+{int(height/5)}'
    
    root = Tk()
    root.geometry(geometry_str)
    root.call('wm', 'attributes', '.', '-topmost', True)
    filenames = filedialog.askopenfilenames() # show an "Open" dialog box and return the path to the selected file
    root.destroy()
    return filenames

def split_pdf():
    pdfs = get_filenames()
    for pdf in pdfs:
        basefld = os.path.dirname(pdf) + '/'
        pdf_name = os.path.basename(pdf).split('.')[0]
        pdf_to_split = PdfFileReader(open(pdf, "rb"))
        for i in range(pdf_to_split.numPages):
            pdf_out = PdfFileWriter()
            pdf_out.addPage(pdf_to_split.getPage(i))
            with open(basefld + pdf_name + "-page%s.pdf" % i, "wb") as outputStream:
                pdf_out.write(outputStream)

def merge_pdf():
    pdfs = get_filenames()
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    basefld = os.path.dirname(pdfs[0]) + '/'
    merger.write(basefld + 'result.pdf')
    merger.close()
