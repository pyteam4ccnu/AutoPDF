from .merge import merge_pdf
import os


def run_merge():
    """
    This function means to run the merge action.
    :return:
    """
    dir = os.environ.get("AutoPDF_PDFdir") or "/home/song-ruyang/AutoPDF/download"
    output = os.environ.get("AutoPDF_NewPDFname") or "PythonBook.pdf"
    merge_pdf(dir, output)
