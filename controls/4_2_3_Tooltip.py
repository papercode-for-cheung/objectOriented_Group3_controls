#显示控件提示信息

import sys#获取api
from PyQt5.QtWidgets import QMainWindow,QToolTip,QApplication,QHBoxLayout,QWidget,QPushButton  #QHBoxLayout:水平布局，QWidget：控件
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #设置字体
        QToolTip.setFont(QFont('SansSerif',12))
        #设置提示内容
        #self.setToolTip('这是面向对象技术的课程')
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('设置控件提示信息')

        # 设置Button
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮')
        # 将按钮放在窗口上，使用水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFram = QWidget()
        mainFram.setLayout(layout)

        self.setCentralWidget(mainFram)
        

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = TooltipForm()
   #显示窗口
   main.show()

   sys.exit(app.exec_())




