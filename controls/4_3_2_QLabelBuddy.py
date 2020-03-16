"""
案例4-8
QLabel与伙伴控件
伙伴关系：通过QLabel的热键(&)来控制其他的控件
之前已经通过可视化方法QDesigner设置过，但是内在的代码原理我们还是不懂，现在是要通过python代码去实现伙伴关系
"""
from PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog): #QDialog:对话框的基类
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴关系')

        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)#放在第一行第一列
        mainLayout.addWidget(nameLineEdit,0,1,1,2)#放在第一行第二列，占用一行两列

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QLabelBuddy()
   #显示窗口
   main.show()

   sys.exit(app.exec_())