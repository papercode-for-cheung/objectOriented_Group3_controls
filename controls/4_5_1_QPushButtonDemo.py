"""
案例4-14
按钮控件（QPushButton）

"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QPushButtonDemo(QDialog):#把QDialog作为一个对话框
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
       self.setWindowTitle('QPushButton  Demo')

       #使用垂直布局
       layout = QVBoxLayout()

       self.button1 = QPushButton('第一个按钮')#显示文本可以后期设置
       #self.button1.setText('First Button')

       # 设置开关:（toggle方法）按钮不会自动抬起，按钮按下时不自动抬起，再次点击时才会抬起
       self.button1.setCheckable(True)#按钮是可复选的
       self.button1.toggle()
       #self.button1.clicked.connect(self.whichButton)#报错
       self.button1.clicked.connect(lambda :self.whichButton(self.button1))
       self.button1.clicked.connect(self.buttonState)
       layout.addWidget(self.button1)

        #在文本前显示是图像
       self.button2 = QPushButton('图像按钮')
       self.button2.setIcon(QIcon(QPixmap('./images/SDAU.jpg')))
       self.button2.clicked.connect(lambda :self.whichButton(self.button2))
       layout.addWidget(self.button2)

       #按钮不可用，调用setEnable
       self.button3 = QPushButton('不可用的按钮')
       self.button3.setEnabled(False)
       layout.addWidget(self.button3)

       #设置默认按钮，窗口显示时，按回车，自动调用默认按钮,一个窗口只能有一个默认按钮
       self.button4 = QPushButton('&MyButton')#热键
       self.button4.setDefault(True)
       self.button4.clicked.connect(lambda: self.whichButton(self.button4))
       layout.addWidget(self.button4)


       self.setLayout(layout)
       self.resize(400,300)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮一已经被选中')
        else:
            print('按钮一未被选中')

    #哪个按钮点击了，
    # 方法1：不传参数
    # def whichButton(self):
    #     sender = self.sender()
    #     print(sender.text() + "按钮被按下")
    #方法2：
    def whichButton(self,btn):
        print('被单击的按钮是：' + btn.text())



if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QPushButtonDemo()
   #显示窗口
   main.show()

   sys.exit(app.exec_())
