"""
案例4-15
单选按钮控件 QRadioButton
"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.intiUI()

    def intiUI(self):
        self.setWindowTitle('QRadioButton')
        #放置两个单选控件，放在一个容器内
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setCheckable(True) #默认该按钮为选中
        #连接信号与槽，
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.setCheckable(True)  # 默认该按钮为选中
        # 连接信号与槽，
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)

        self.setLayout(layout)


    #槽函数：判断哪个按钮被点击
    def buttonState(self):
        radioButton = self.sender()
        if radioButton.text() == '单选按钮1':
            if radioButton.isChecked() == True:
                print(radioButton.text() + '被选中')
            else:
                print(radioButton.text() + '被取消选中')

        if radioButton.text() == '单选按钮2':
            if radioButton.isChecked() == True:
                print(radioButton.text() + '被选中')
            else:
                print(radioButton.text() + '被取消选中')


if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QRadioButtonDemo()
   #显示窗口
   main.show()

   sys.exit(app.exec_())