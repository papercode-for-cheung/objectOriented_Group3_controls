"""
案例4-10
限制QLineEdit控件的输入（校验器）
"""
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        #创建表单布局
        formLayout = QFormLayout()

        #创建控件
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        #将控件加入表单中
        formLayout.addRow('整数类型',intLineEdit)
        formLayout.addRow('浮点数类型', doubleLineEdit)
        formLayout.addRow('数字和字母', validatorLineEdit)

        #设置placeholdertext
        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点数')
        validatorLineEdit.setPlaceholderText('数字和字母')

        #整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)#设置整数校验器的整数范围为1-99

        #浮点校验器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360)#设置浮点数校验器的整数范围为-360-+360
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)#正常表示浮点数
        #设置浮点数的精度,小数点后2位
        doubleValidator.setDecimals(2)

        #字符和数字校验器
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QLineEditValidator()
   #显示窗口
   main.show()

   sys.exit(app.exec_())
