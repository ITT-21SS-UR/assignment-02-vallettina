import sys
from PyQt5 import uic, Qt
from PyQt5.QtWidgets import QMainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calculator.ui", self)
        self.initButtons()

    def initButtons(self):
        # clear text
        self.ui.lcd_result.setText("")
        # number buttons
        self.ui.btn_0.clicked.connect(self.action_0)
        self.ui.btn_1.clicked.connect(self.action_1)
        self.ui.btn_2.clicked.connect(self.action_2)
        self.ui.btn_3.clicked.connect(self.action_3)
        self.ui.btn_4.clicked.connect(self.action_4)
        self.ui.btn_5.clicked.connect(self.action_5)
        self.ui.btn_6.clicked.connect(self.action_6)
        self.ui.btn_7.clicked.connect(self.action_7)
        self.ui.btn_8.clicked.connect(self.action_8)
        self.ui.btn_9.clicked.connect(self.action_9)
        # arithmetic signs
        self.ui.btn_equals.clicked.connect(self.action_equals)
        self.ui.btn_plus.clicked.connect(self.action_plus)
        self.ui.btn_minus.clicked.connect(self.action_minus)
        self.ui.btn_div.clicked.connect(self.action_div)
        self.ui.btn_multi.clicked.connect(self.action_multi)
        # other buttons
        self.ui.btn_clean.clicked.connect(self.action_clean)
        self.ui.btn_delete.clicked.connect(self.action_delete)
        self.ui.btn_point.clicked.connect(self.action_point)

    # number methods
    def action_0(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "0")
        print(equation + "0")

    def action_1(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "1")
        print(equation + "1")

    def action_2(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "2")
        print(equation + "2")

    def action_3(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "3")
        print(equation + "3")

    def action_4(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "4")
        print(equation + "4")

    def action_5(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "5")
        print(equation + "5")

    def action_6(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "6")
        print(equation + "6")

    def action_7(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "7")
        print(equation + "7")

    def action_8(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "8")
        print(equation + "8")

    def action_9(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "9")
        print(equation + "9")

    # arithmetic signs
    def action_plus(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "+")
        print(equation + "+")

    def action_minus(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "-")
        print(equation + "-")

    def action_multi(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "*")
        print(equation + "*")

    def action_div(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + "/")
        print(equation + "/")

    def action_equals(self):
        equation = self.ui.lcd_result.text()

        try:
            result = eval(equation)
            self.ui.lcd_result.setText(str(result))
            print(result)
        except:
            self.ui.lcd_result.setText("ERROR")
            print("ERROR")

    # other buttons
    def action_point(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation + ".")
        print(equation + ".")

    def action_delete(self):
        equation = self.ui.lcd_result.text()
        self.ui.lcd_result.setText(equation[:len(equation) - 1])
        print(equation[:len(equation) - 1])

    def action_clean(self):
        self.ui.lcd_result.setText("")
        print("")


def main():
    app = Qt.QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
