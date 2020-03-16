"""
案例4-16
复选框控件 QCheckBox
三种状态：checkState()
未选中：0
半选中：1
选中：2

水平放置三个复选框控件，来模拟这三个状态
"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')

        layout = QHBoxLayout()

        self.checkbox1 = QCheckBox('复选框控件1')
        self.checkbox1.setCheckable(True)
        self.checkbox1.stateChanged.connect(lambda :self.checkboxState(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox('复选框控件2')
        self.checkbox2.stateChanged.connect(lambda: self.checkboxState(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox('半选中')
        self.checkbox3.stateChanged.connect(lambda: self.checkboxState(self.checkbox3))
        #设置半选中状态
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkbox3)

        self.setLayout(layout)

    #捕捉按钮状态
    def checkboxState(self,cb):
        check1State = self.checkbox1.text() + ',isChechked=' + str(self.checkbox1.isChecked()) + ',chechkState=' + str(self.checkbox1.checkState()) + '\n' #checkState返回状态
        check2State = self.checkbox2.text() + ',isChechked=' + str(self.checkbox2.isChecked()) + ',chechkState=' + str(self.checkbox2.checkState()) + '\n'
        check3State = self.checkbox3.text() + ',isChechked=' + str(self.checkbox3.isChecked()) + ',chechkState=' + str(self.checkbox3.checkState()) + '\n'
        print(check1State + check2State + check3State)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QCheckBoxDemo()
   #显示窗口
   main.show()

   sys.exit(app.exec_())