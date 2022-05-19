import threading

import numpy as np
from PySide6.QtWidgets import *
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from NMEA_Socket import Nmea_Tcp


class GNSS_DRAW(QMainWindow, Nmea_Tcp):

    def __init__(self):
        super(GNSS_DRAW, self).__init__()
        Nmea_Tcp.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("gnss_tool")
        self.static_canvas = FigureCanvas(Figure(figsize=(3, 3)))
        self.layout = QGridLayout(self.satellite_view)
        self.layout.addWidget(self.static_canvas, 1, 1)

    def init_gnss_draw(self, gnss_signal):
        Sat_view = threading.Thread(target=self.sat_view)
        Sat_view.start()
        '''
        gnss_signal={'GPS': [['05', '43', '082', '41'], ['13', '43', '036', '45'], ['15', '68', '343', '41'], ['18',
        '56', '303', '31']], 'GAL': [['05', '18', '053', '39'], ['03', '62', '010', '47']], 'GLO': [['72', '34',
        '035', '39'], ['74', '27', '071', '40'], ['65', '45', '327', '37']], 'BDS': [['08', '79', '027', '36'],
        ['13', '69', '336', '36'], ['20', '53', '031', '50'], ['32', '13', '076', '38'], ['37', '33', '081', '42'],
        ['19', '44', '306', '33']]}
        self.sat_view(gnss_signal)
        '''

    def sat_view(self):
        FuncAnimation(self.static_canvas.figure, func=self.animate, interval=2000)

    def animate(self, gnss_signal: dict):
        self.static_canvas.figure.clear()
        ax = self.static_canvas.figure.add_subplot(111, projection='polar')  # projection='polar'-->设为极坐标

        ax.set_theta_direction(-1)  # 设置极坐标⽅向：1->顺时针；-1->逆时针
        ax.set_theta_zero_location('N')  # 设置极⾓初始值位置（默认是东-->右侧）
        ax.yaxis.set_label_position('right')
        ax.tick_params('y', labelleft=False)  # 不显⽰极径刻度值
        ax.grid(linestyle='--')  # 设置线型
        labels = ['N', '45°', 'E', '135°', 'S', '225°', 'W', '315°']
        ax.set_thetagrids(range(0, 360, 45), labels, fontweight='semibold')  # 设置极⾓显⽰的刻度值
        ax.set_rlim(90, 0)
        #    SATAZ：卫星的⽅位⾓, SATEL：卫星的⾼度⾓

        GPSAZ, GPSEL, GPSCN0, GALAZ, GALEL, GALCN0, GLOAZ, GLOEL, GLOCN0, BDSAZ, BDSEL, BDSCN0, GPSID, GALID, GLOID, BDSID = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        '''
            以下列表中，GPSID代表卫星PN，GPSEL代表卫星高度角，GPSAZ代表卫星方位角，GPSCN0代表设备的CN0
            '''
        for num_gps in range(0, len(gnss_signal["GPS"])):

            if gnss_signal["GPS"][num_gps][3] != '':
                GPSID.append(gnss_signal["GPS"][num_gps][0])
                if gnss_signal["GPS"][num_gps][1] != '':
                    GPSEL.append(int(gnss_signal["GPS"][num_gps][1]))
                else:
                    GPSEL.append(0)
                if gnss_signal["GPS"][num_gps][2] != '':
                    GPSAZ.append(int(gnss_signal["GPS"][num_gps][2]))
                else:
                    GPSAZ.append(0)
                GPSCN0.append(int(gnss_signal["GPS"][num_gps][3]))
        for num_gal in range(0, len(gnss_signal["GAL"])):

            if gnss_signal["GAL"][num_gal][3] != '':
                if gnss_signal["GAL"][num_gal][0] != '':
                    GALID.append(gnss_signal["GAL"][num_gal][0])
                else:
                    GALID.append("？")
                if gnss_signal["GAL"][num_gal][1] != '':
                    GALEL.append(int(gnss_signal["GAL"][num_gal][1]))
                else:
                    GALEL.append(0)
                if gnss_signal["GAL"][num_gal][2] != '':
                    GALAZ.append(int(gnss_signal["GAL"][num_gal][2]))
                else:
                    GALAZ.append(0)
                GALCN0.append(int(gnss_signal["GAL"][num_gal][3]))
        for num_glo in range(0, len(gnss_signal["GLO"])):
            if gnss_signal["GLO"][num_glo][3] != '':
                if gnss_signal["GLO"][num_glo][0]:
                    GLOID.append(gnss_signal["GLO"][num_glo][0])
                else:
                    GLOID.append("?")
                if gnss_signal["GLO"][num_glo][1] != "":
                    GLOEL.append(int(gnss_signal["GLO"][num_glo][1]))
                else:
                    GLOEL.append(0)
                if gnss_signal["GLO"][num_glo][2] != '':
                    GLOAZ.append(int(gnss_signal["GLO"][num_glo][2]))
                else:
                    GLOAZ.append(0)
                GLOCN0.append(int(gnss_signal["GLO"][num_glo][3]))
        for num_bds in range(0, len(gnss_signal["BDS"])):

            if gnss_signal["BDS"][num_bds][3] != '':
                if gnss_signal["BDS"][num_bds][0] != '':
                    BDSID.append(str(int(gnss_signal["BDS"][num_bds][0]) - 140))
                else:
                    BDSID.append("?")
                if gnss_signal["BDS"][num_bds][1] != '':
                    BDSEL.append(int(gnss_signal["BDS"][num_bds][1]))
                else:
                    BDSEL.append(0)
                if gnss_signal["BDS"][num_bds][2] != '':
                    BDSAZ.append(int(gnss_signal["BDS"][num_bds][2]))
                else:
                    BDSAZ.append(0)
                BDSCN0.append(int(gnss_signal["BDS"][num_bds][3]))
        '''
            将方位角转换为弧度
            '''

        gpsaz = list(map(lambda i: int(i) * 2 * np.pi / 360, GPSAZ))
        galaz = list(map(lambda i: int(i) * 2 * np.pi / 360, GALAZ))
        gloaz = list(map(lambda i: int(i) * 2 * np.pi / 360, GLOAZ))
        bdsaz = list(map(lambda i: int(i) * 2 * np.pi / 360, BDSAZ))
        '''
            画图展示，gps红色#FF6A6A，bds绿色#4EEE94，gal蓝色#7B68EE，glo棕色#FFD700
            '''
        ax.scatter(gpsaz, GPSEL, marker=".", s=450, c='#FF6A6A', alpha=0.75,
                   label='GPS')  # ⽤来画散点图，marker-->控制点的形状， alpha-->控制透明度（0-1）
        for i in range(0, len(gpsaz)):
            ax.text(gpsaz[i], GPSEL[i], GPSID[i], ha="center", va="center", fontsize=8)

        ax.scatter(galaz, GALEL, marker=".", s=450, c='#7B68EE', alpha=0.75,
                   label='GAL')  # ⽤来画散点图，marker-->控制点的形状， alpha-->控制透明度（0-1）
        for i in range(0, len(galaz)):
            ax.text(galaz[i], GALEL[i], GALID[i], ha="center", va="center", fontsize=8)

        ax.scatter(gloaz, GLOEL, marker=".", s=450, c='#FFD700', alpha=0.75,
                   label='GLO')  # ⽤来画散点图，marker-->控制点的形状， alpha-->控制透明度（0-1）
        for i in range(0, len(gloaz)):
            ax.text(gloaz[i], GLOEL[i], GLOID[i], ha="center", va="center", fontsize=8)

        ax.scatter(bdsaz, BDSEL, marker=".", s=450, c='#4EEE94', alpha=0.75,
                   label='BDS')  # ⽤来画散点图，marker-->控制点的形状， alpha-->控制透明度（0-1）
        for i in range(0, len(bdsaz)):
            ax.text(bdsaz[i], BDSEL[i], BDSID[i], ha="center", va="center", fontsize=8)

        ax.set_rticks(range(90, 0, -10))  # 极坐标标签显⽰范围
        ax.legend(bbox_to_anchor=(1.1, 1.15), frameon=False, fontsize="xx-small")
        self.static_canvas.draw()
        self.static_canvas.flush_events()
        # time.sleep(1)

    # plt.ioff()
    # plt.show()


if __name__ == '__main__':
    app = QApplication([])
    stats = GNSS_DRAW()
    stats.show()
    app.exec()
