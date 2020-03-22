"""
案例4-7
QLabel控件
"""

import sys
from PyQt5.QtWidgets import QLabel,QMainWindow,QApplication,QVBoxLayout,QWidget,QPushButton  #QHBoxLayout:水平布局，QWidget：控件
from PyQt5.QtGui import QPixmap,QPalette  #调色板
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        #设置文本标签
        label1.setText("<font color=yellow>这是一个文本标签</font>")   #setText支持HTML标签
        label1.setAutoFillBackground(True)#设置自动填充背景
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)#设置文本对齐方式

        label2.setText("<a href = '#'>欢迎使用python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./images/SDAU2.jpg'))

        # 当参数为True时，响应a标签的内容，当参数为False时，响应与槽绑定的信号
        label4.setOpenExternalLinks(False)

        label4.setText("<a href='http://www.dlu.edu.cn/'>欢迎来到大连大学</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        #使用垂直布局进行布局显示
        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        #绑定信号与槽
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')


    #划过标签的方法（槽）
    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    #单击标签的方法（槽）
    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')

if __name__ == '__main__':
   app = QApplication(sys.argv)
   main = QLabelDemo()
   #显示窗口
   main.show()

   sys.exit(app.exec_())




