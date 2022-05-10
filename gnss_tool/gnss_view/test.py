'''
import numpy as np
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
from gnss_tool.UI.ui_mian import Ui_MainWindow


class Mytest(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mytest, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("gnss_tool")

    def init(self):
        # self.figure = plt.figure()
        self.static_canvas = FigureCanvas(Figure(layout="tight"))
        # self.static_canvas = FigureCanvas(self.figure)
        self.static_canvas.figure.get_default_bbox_extra_artists()
        self.layout = QGridLayout(self.satellite_view)
        self.layout.addWidget(self.static_canvas, 1, 1)
        self.layout.addWidget(NavigationToolbar(self.static_canvas,self))
        self._static_ax1, self._static_ax2 = self.static_canvas.figure.subplots(2, 1)
        t = np.linspace(0, 10, 501)
        self._static_ax1.plot(t, np.tan(t), ".")

        self.timer1 = QTimer()
        self.timer1.start(100)
        self.i = 0
        self.t = []
        self.s = []


if __name__ == '__main__':
    app = QApplication([])
    stats = Mytest()
    stats.show()
    app.exec()
'''
import numpy as np
import math
import matplotlib.pyplot as plt

ax = plt.subplot(111, projection='polar')  # projection='polar'-->设为极坐标
ax.set_theta_direction(-1)  # 设置极坐标⽅向：1->顺时针；-1->逆时针
ax.set_theta_zero_location('N')  # 设置极⾓初始值位置（默认是东-->右侧）
ax.yaxis.set_label_position('right')
ax.tick_params('y', labelleft=False)  # 不显⽰极径刻度值
ax.grid(linestyle='--')  # 设置线型
labels = ['N', '45°', 'E', '135°', 'S', '225°', 'W', '315°']
ax.set_thetagrids(range(0, 360, 45), labels, fontweight='semibold')  # 设置极⾓显⽰的刻度值
ax.set_rlim(90, 0)
#     SATAZ：卫星的⽅位⾓, SATEL：卫星的⾼度⾓
SATAZ = [0, 30, 55, 0, 110, 0]
s = list(map(lambda i: int(i) * 2 * np.pi / 360, SATAZ))
print(s)
# 卫星的空天图和极径⽅向正好相反，所以刻度值是⾃⼰画的
SATEL = [0, 15, 30, 45, 60, 75]
SATID = ['90', '75', '60', '45', '30', '15']
b1 = [44, 56, 78, 23, 55, 23]
b2 = [60, 130, 255, 340, 110, 40]
c = ax.scatter(s, SATEL, marker=".", s=450, c='#4EEE94', alpha=0.75,
               label='GPS')  # ⽤来画散点图，marker-->控制点的形状， alpha-->控制透明度（0-1）
d = ax.scatter(b2, b1, marker=".", s=450, c='#6A5ACD', alpha=0.75, label='BDS')

for i in range(0, 6):
    ax.text(s[i], SATEL[i], SATID[i], ha="center", va="center", fontsize=8)  # 画极径刻度值（⽅法有点low）
    ax.text(b2[i], b1[i], SATID[i], ha="center", va="center", fontsize=8)
ax.set_rticks(range(90, 0, -10))  # 极坐标标签显⽰范围
plt.legend(bbox_to_anchor=(1.2, 1), frameon=False, fontsize="xx-small")
plt.show()
