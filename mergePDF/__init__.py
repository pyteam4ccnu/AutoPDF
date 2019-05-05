from .merge import merge_pdf


def run_merge():
    dir = "/home/song-ruyang/AutoPDF/download"
    output = "PythonBook.pdf"
    merge_pdf(dir, output)
