import sys

from PyQt5.QtWidgets import *
from .form import Form


def run_view(run_app, merge_pdf):
    """
    For package view's running: Creating QtWindow, Showing it and Exiting handler.
    :param run_app: The MAIN FUNCTION for downloading PDFs.
    :param merge_pdf: The PDFs's merger.
    :return:
    """
    app = QApplication(sys.argv)
    demo = Form(run_function=run_app, merge_function=merge_pdf)
    demo.show()
    sys.exit(app.exec_())
