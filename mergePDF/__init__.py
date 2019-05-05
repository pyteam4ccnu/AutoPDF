from .merge import merge_pdf


def run_merge():
    """
    This function means to run the merge action.
    :return:
    """
    dir = "/home/song-ruyang/AutoPDF/download"
    output = "PythonBook.pdf"
    merge_pdf(dir, output)
