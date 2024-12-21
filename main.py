from PyQt5.QtWidgets import QApplication
from layout import Layout

class App(Layout):

    def __init__(self):
        super().__init__()

        self.AppLayout = Layout()

        for btn in self.buttons:
            btn.clicked.connect(self.click_event)
        
        self.clear_btn.clicked.connect(self.click_event)
        self.delete_btn.clicked.connect(self.click_event)

    def click_event(self):
        click = self.sender()

        if click.text() == "Clear":
            self.input_box.clear()
            self.input_box.setPlaceholderText("0")
        elif click.text() == "<":
            exp = self.input_box.text()
            self.input_box.setText(exp[:-1])
        elif click.text() == "=":
            exp = self.input_box.text()
            try:
                evl = eval(exp)
                self.input_box.setText(str(evl))
            except ZeroDivisionError as e:
                self.input_box.clear()
                self.input_box.setPlaceholderText("Error: " + str(e))
            except Exception as e:
                self.input_box.clear()
                self.input_box.setPlaceholderText("Error: " + str(e)[:-19])
        else:
            exp = self.input_box.text()
            new_chr = click.text()
            self.input_box.setText(exp + new_chr)
        
        
if __name__ == "__main__":
    app = QApplication([])
    main_app = App()
    main_app.show()
    app.exec_()
