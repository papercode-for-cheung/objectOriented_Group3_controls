"""
案例4-1
创建一个主窗口
"""


import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QTextEdit,QAction
from PyQt5.QtGui import QIcon #图标


"""创建一个类，从主窗口QMainWindow继承"""
class FirstMainWin(QMainWindow):
#class FirstMainWin(QDialog):
    def __init__(self):

        super(FirstMainWin, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口的尺寸
        self.resize(400, 300)

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        #创建基本事件
        exitAct = QAction(QIcon('./images/SDAU.jpg'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        #创建菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        #创建工具栏
        toolBar = self.addToolBar("Exit")
        toolBar.addAction(exitAct)

        # 获取状态栏
        self.status = self.statusBar()
        # 状态栏显示消息，showMessage():5000毫秒
        self.status.showMessage('只存在5秒的消息', 5000)
        #self.setWindowIcon(QIcon('./images/SDAU.jpg'))


if __name__ == '__main__':
    #创建QApplication对象
   app = QApplication(sys.argv)
   #设置应用程序的图标
   app.setWindowIcon(QIcon('./images/SDAU.jpg'))
   main = FirstMainWin()
   #显示窗口
   main.show()

   sys.exit(app.exec_())
