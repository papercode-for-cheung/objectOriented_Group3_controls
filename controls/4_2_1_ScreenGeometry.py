"""
案例4-4
屏幕坐标系
"""
import sys#获取api
from PyQt5.QtWidgets import QMainWindow,QApplication,QHBoxLayout,QWidget,QPushButton  #QHBoxLayout:水平布局，QWidget：控件

app = QApplication(sys.argv)

def onClick_Button():
    print("QWidget")#
    print("widget.x() = %d" % widget.x())   #窗口横坐标
    print("widget.y() = %d" % widget.y())   #窗口纵坐标
    print("widget.width() = %d" % widget.width())   #工作区宽度
    print("widget.height() = %d" % widget.height())     #工作区高度
    print("geometry")#通过坐标系获取工作区的面积
    print("widget.geometry().x() = %d" % widget.geometry().x())     #工作区横坐标
    print("widget.geometry().y() = %d" % widget.geometry().y())     #工作区纵坐标
    print("widget.geometry().width() = %d" % widget.geometry().width())     #工作区宽度
    print("widget.geometry().height() = %d" % widget.geometry().height())   #工作区高度
    print("frameGeometry")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())   #窗口横坐标
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())   #窗口纵坐标
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width())   #窗口宽度
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height()) #窗口高度


widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

btn.move(24,52)
widget.resize(300,240)#设置工作区的尺寸
#设置工作区的尺寸（不可变）
#widget.setFixedSize(200,200)
widget.move(250,200)
widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())


