"""
案例4-6
设置窗口图标
"""


import sys#获取api
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon #图标

class IconForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #设置窗口位置和大小，setGeometry（），前两个参数是窗口的左上角的坐标，后两个参数是窗口的大小
        self.setGeometry(300,300,250,250)
        #设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        #设置窗口图标
        self.setWindowIcon(QIcon('./images/SDAU.jpg'))#窗口的setWindowIcon设置的图标可以在Windows系统下显示


if __name__ == '__main__':
   app = QApplication(sys.argv)
   #设置应用程序的图标
   #app.setWindowIcon(QIcon('./images/SDAU.jpg'))
   main = IconForm()
   #显示窗口
   main.show()

   sys.exit(app.exec_())
