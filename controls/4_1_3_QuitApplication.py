"""
案例4-3
退出应用程序
"""

import sys#获取api
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QWidget,QPushButton  #QHBoxLayout:水平布局，QWidget：控件

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        #设置Button
        self.button1 = QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        #将按钮放在窗口上，使用水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFram =  QWidget()
        mainFram.setLayout(layout)

        self.setCentralWidget(mainFram)

    #按钮单击事件的方法(自定义的槽【相当于事件的一个方法】)
    def onClick_Button(self):
        sender= self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        #退出应用程序
        app.quit()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QuitApplication()
   #显示窗口
   main.show()

   sys.exit(app.exec_())
