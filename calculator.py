# Implement a simple graphical calculator using PyQt.
# Source for the basic structure of the calculator: https://www.geeksforgeeks.org/building-calculator-using-pyqt5-in-python/


import sys
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calculator.ui", self)
        self.init_buttons()

    def init_buttons(self):
        # clear text
        self.ui.lcd_result.setText("")
        # number buttons
        self.ui.btn_0.clicked.connect(lambda x: self.action('0'))
        self.ui.btn_1.clicked.connect(lambda x: self.action('1'))
        self.ui.btn_2.clicked.connect(lambda x: self.action('2'))
        self.ui.btn_3.clicked.connect(lambda x: self.action('3'))
        self.ui.btn_4.clicked.connect(lambda x: self.action('4'))
        self.ui.btn_5.clicked.connect(lambda x: self.action('5'))
        self.ui.btn_6.clicked.connect(lambda x: self.action('6'))
        self.ui.btn_7.clicked.connect(lambda x: self.action('7'))
        self.ui.btn_8.clicked.connect(lambda x: self.action('8'))
        self.ui.btn_9.clicked.connect(lambda x: self.action('9'))
        # arithmetic signs
        self.ui.btn_equals.clicked.connect(lambda x: self.action('='))
        self.ui.btn_plus.clicked.connect(lambda x: self.action('+'))
        self.ui.btn_minus.clicked.connect(lambda x: self.action('-'))
        self.ui.btn_div.clicked.connect(lambda x: self.action('/'))
        self.ui.btn_multi.clicked.connect(lambda x: self.action('*'))
        # other buttons
        self.ui.btn_clean.clicked.connect(lambda x: self.action('CLEAN'))
        self.ui.btn_delete.clicked.connect(lambda x: self.action('DELETE'))
        self.ui.btn_point.clicked.connect(lambda x: self.action('.'))


    def log_button(message):
        def func_decorator(func):
            def logging(self, sign):
                print(message + sign)
                func(self, sign)
            return logging
        return func_decorator

    @log_button("Button clicked: ")
    def action(self, sign):
        equation = self.ui.lcd_result.text()

        if sign in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.ui.lcd_result.setText(equation + sign)

        if sign in [".", "+", "-", "*", "/"]:
            self.ui.lcd_result.setText(equation + sign)

        if sign == "DELETE":
            self.ui.lcd_result.setText(equation[:len(equation) - 1])

        if sign == "CLEAN":
            self.ui.lcd_result.setText("")

        if sign == "=":
            try:
                result = eval(equation)
                self.ui.lcd_result.setText(str(result))
            except:
                self.ui.lcd_result.setText("ERROR")
                print("ERROR")


def main():
    app = Qt.QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
