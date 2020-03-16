import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ComboxDemo(QWidget):
    def __init__(self,parent=None):
        super(ComboxDemo,self).__init__(parent)
        self.setWindowTitle("ComBox 例子")
        self.resize(300,90)
        layout = QVBoxLayout()
        self.lbl = QLabel("")

        self.cb = QComboBox()
        # 添加一个下拉选项
        self.cb.addItem("C")
        self.cb.addItem("C++")
        # 添加多个下拉选项
        self.cb.addItems(["Java", "C#", "Python"])
        # 选项改变时发射currentIndexChanged信号，连接到自定义的函数selectionchange()
        self.cb.currentIndexChanged.connect(self.selectionchange)
        layout.addWidget(self.cb)
        layout.addWidget(self.lbl)
        self.setLayout(layout)

    def selectionchange(self, i):
        # 将选项的文本设置为标签的文本，并调整标签大小
        self.lbl.setText(self.cb.currentText())
        print("Items in the list are :")
        for count in range(self.cb.count()):
            print('item'+str(count) +'='+ self.cb.itemText(count))
            print("Current index",i,"selection changed",self.cb.currentText())

if __name__=='__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec())


