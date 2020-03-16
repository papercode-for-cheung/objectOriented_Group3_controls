"""
案例4-9
QLineEdit控件与回显模式（EchoMode）

QLineEdit控件：
基本功能：输入单行文本
高级功能：设置回显模式（EchoMode）、设置掩码

"""

from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        formLayout = QFormLayout()

        #创建4个控件
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        #将控件加入表单中，按行加入
        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit", passwordEchoOnEditLineEdit)

        #为每个文本输入框设置placeholdertext，用途：在没有输入时以灰色显示文本输入框是做什么的,输入内容时提示消失
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        #设置显示模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QLineEditEchoMode()
   #显示窗口
   main.show()

   sys.exit(app.exec_())