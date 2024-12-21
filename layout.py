from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt

class Layout(QWidget):

    def __init__(self):
        super().__init__()

        # main Window
        self.setWindowTitle("Calculator")
        self.resize(500,500)

        # All Widgets/objects
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("0")
        self.button_grid = QGridLayout()
        self.clear_btn = QPushButton("Clear")
        self.delete_btn = QPushButton("<")

        # Design
        self.masterLayout = QVBoxLayout()
        self.buttonRow = QHBoxLayout()
        

        self.masterLayout.addWidget(self.input_box)
        row = 0
        col = 0
        button_label = ["7", "8", "9", "/", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "=", "*"]
        self.buttons = []

        for btnLabel in button_label:
            btn = QPushButton(btnLabel)
            self.button_grid.addWidget(btn, row, col)
            self.buttons.append(btn)
            col += 1

            if col > 3:
                col = 0
                row += 1
        
        self.masterLayout.addLayout(self.button_grid)
        self.buttonRow.addWidget(self.clear_btn)
        self.buttonRow.addWidget(self.delete_btn)
        self.masterLayout.addLayout(self.buttonRow)

        with open("style.qss", "r") as styleSheet:
            self.setStyleSheet(styleSheet.read())

        self.setLayout(self.masterLayout)