from PySide import QtCore, QtGui
import sys, string
import time
from random import choice as rndchoice

class mainWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        super(mainWindow, self).__init__(parent)

        self.setMinimumSize(320, 600)
        self.resize(320, 600)

        self.frame = QtGui.QVBoxLayout(self)
        self.frame.setContentsMargins(0, 0, 0, 0)
        self.frame.setSpacing(0)
        self.frame.setAlignment(QtCore.Qt.AlignTop)

        self.settings = QtGui.QVBoxLayout()
        self.settings.setContentsMargins(10, 10, 10, 10)
        self.settings.setSpacing(10)

        self.body = QtGui.QVBoxLayout()
        self.body.setContentsMargins(10, 10, 10, 10)
        self.body.setSpacing(10)

        self.accepted_char_layout = QtGui.QVBoxLayout()
        self.accepted_char_layout.setContentsMargins(10, 10, 10, 10)
        self.accepted_char_layout.setSpacing(10)
        self.accepted_char_layout.setAlignment(QtCore.Qt.AlignTop)

        self.output_layout = QtGui.QVBoxLayout()
        self.output_layout.setContentsMargins(10, 10, 10, 10)
        self.output_layout.setSpacing(10)
        self.output_layout.setAlignment(QtCore.Qt.AlignTop)

        self.settings_group = QtGui.QGroupBox("Settings")
        self.accepted_char_group = QtGui.QGroupBox("Accepted Characters")
        self.output_group = QtGui.QGroupBox("Passwords")

        self.pass_count = QtGui.QSpinBox()
        self.pass_count.setMinimum(1)
        self.pass_count.setMaximum(9999)
        self.pass_count.setValue(5)

        self.pass_count.setFixedWidth(64)

        self.pass_length = QtGui.QSpinBox()
        self.pass_length.setMinimum(1)
        self.pass_length.setMaximum(9999)
        self.pass_length.setValue(32)

        self.pass_length.setFixedWidth(64)

        self.gen_button = QtGui.QPushButton("Generate")
        self.gen_button.pressed.connect(self.generate)

        self.settings.addWidget(QtGui.QLabel("Number of Passwords"))
        self.settings.addWidget(self.pass_count)
        self.settings.addWidget(QtGui.QLabel("Length of Passwords"))
        self.settings.addWidget(self.pass_length)
        self.settings.addWidget(self.gen_button)

        self.accepted_char_edit = QtGui.QTextEdit()
        self.accepted_char_edit.setText(string.ascii_uppercase +
                                        string.ascii_lowercase +
                                        string.digits +
                                        string.punctuation)

        self.output_edit = QtGui.QTextEdit()

        self.accepted_char_layout.addWidget(self.accepted_char_edit)
        self.output_layout.addWidget(self.output_edit)

        self.settings_group.setLayout(self.settings)
        self.accepted_char_group.setLayout(self.accepted_char_layout)
        self.output_group.setLayout(self.output_layout)

        self.body.addWidget(self.settings_group)
        self.body.addWidget(self.accepted_char_group)
        self.body.addWidget(self.output_group)

        self.frame.addLayout(self.body)

    def generate(self):
        if not len(self.accepted_char_edit.toPlainText()):
            return

        self.output_edit.setText("")
        for i in xrange(self.pass_count.value()):
            password = ""
            for j in xrange(self.pass_length.value()):
                password += rndchoice(self.accepted_char_edit.toPlainText())

            self.output_edit.setText(self.output_edit.toPlainText() + password + ("\n" * 2))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")
    window = mainWindow()
    window.show()
    app.exec_()
