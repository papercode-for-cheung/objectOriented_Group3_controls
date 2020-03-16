"""
案例4-2
通过QDesktopWidget可以得到整个屏幕的尺寸，计算方法：（屏幕的尺寸-窗口的尺寸）/2
"""


import sys#获取api
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon #图标



class CenterForm(QMainWindow):
    #初始化,parent:把控件放在哪里
    def __init__(self,parent=None):
        super(CenterForm, self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle('让窗口居中')

        #设置窗口的尺寸
        self.resize(400,300)

    def center(self):
        #获取屏幕的坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口的坐标系
        size = self.geometry()
        #计算新窗口的横纵坐标
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        #移动窗口
        self.move(newLeft,newTop)



if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = CenterForm()
   #显示窗口
   main.show()

   sys.exit(app.exec_())
