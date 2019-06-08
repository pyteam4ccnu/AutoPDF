import re

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

url_re = re.compile(
    r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)")
# url_re means to check a string match to a URL.


class Form(QDialog):
    """
    This class is the main window we have: a simple form, made by Header, Two LineEdit and a Button. Thanks for PyQt5.
    :param QDialog: The father class from PyQt5.QtGui, means a Dialog between application and user.
    """
    def __init__(self, run_function=None):
        """
        This function is the init function of Form class, including creating components like Label, LineEdit and Button.
        :param run_function: The run_function means like as you see: just run the MAIN FUNCTION(Download the PDFs).
        """
        super(Form, self).__init__()

        self.run_app = run_function
        self.resize(550, 350)
        self.setWindowTitle('AutoPDF -- The Solution of Python Document Download')
        # Init the main window attributions.

        layout = QVBoxLayout()
        header = QHBoxLayout()

        self.lab = QLabel("- Welcome to AutoPDF -")
        self.lab.setFont(QFont("Times new Roman", 24, QFont.Bold))

        header.addStretch()
        header.addWidget(self.lab)
        header.addStretch()

        self.sub_lab_1 = QLabel("Please input the link:")
        self.sub_lab_1.setFont(QFont("Times new Roman", 12, QFont.Bold))
        self.sub_lab_2 = QLabel("Please input the base:")
        self.sub_lab_2.setFont(QFont("Times new Roman", 12, QFont.Bold))

        self.link_input = QLineEdit()
        self.link_text = ''
        self.base_input = QLineEdit()
        self.base_text = ''

        self.btn = QPushButton("ClickToDownload")
        self.btn.toggle()
        self.btn.clicked.connect(lambda: self.check_and_run())

        layout.setDirection(QBoxLayout.TopToBottom)
        layout.addStretch(2)
        layout.addLayout(header)
        layout.addStretch(3.82)
        layout.addWidget(self.sub_lab_1)
        layout.addWidget(self.link_input)
        layout.addStretch(6.18)
        layout.addWidget(self.sub_lab_2)
        layout.addWidget(self.base_input)
        layout.addStretch(10)
        layout.addWidget(self.btn)
        layout.addStretch(5)

        self.setLayout(layout)

    def check_and_run(self):
        """
        This instant function is a EventListener of Button, means to check the text invalid and run the run_function.
        :return: None
        """
        self.get_input()
        ok = self.check_input()
        if ok:
            self.run()
        else:
            QMessageBox.information(self, "Warning", "URL Invalid!", QMessageBox.Close)

    def get_input(self):
        """
        This function copy the LineEdit text to self buffer.
        :return: None
        """
        self.link_text = self.link_input.text()
        self.base_text = self.base_input.text()
        print(self.link_text, self.base_text)
        return

    def check_input(self):
        """
        Use url_re to check.
        :return: True or False
        """
        return url_re.match(self.link_text) and url_re.match(self.base_text)

    def run(self):
        """
        This function run the run_function, and then create a MessageBox.
        :return: None
        """
        self.run_app(self.link_text, self.base_text)
        QMessageBox.information(self, "Successful", "Download Successful!", QMessageBox.Ok)

