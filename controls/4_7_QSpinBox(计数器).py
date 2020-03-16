import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)
        self.setWindowTitle("SpinBox 例子")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.ll = QLabel("current value:")
        self.ll.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.ll)
        self.sp = QSpinBox()
        layout.addWidget(self.sp)
        # 将计数器的valueChanged信号连接到函数valuechange()
        self.sp.valueChanged.connect(self.valuechange)
        self.setLayout(layout)

    def valuechange(self):
        # valuechange()函数把计数器的当前值设置到标签文本中
        self.ll.setText("current value:" + str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec())

