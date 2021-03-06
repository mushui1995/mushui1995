# coding=utf-8
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from NMEA_Socket import Nmea_Tcp
from gnss_draw import GNSS_DRAW
from gnss_tool.UI.ui_main import Ui_MainWindow
import os


class UI_TOOL_UI(GNSS_DRAW):
    def __init__(self):
        super(UI_TOOL_UI, self).__init__()
        self.init()
        self.receive_show_flag = True  # 是否显示接收到的消息

    def init(self):
        self.connect_device.toggled.connect(self.connect_device_toggled_slot)
        self.connect_device.clicked.connect(self.connect_tcp)
        self.tcp_rev_msg_signal.connect(self.rev_msg)
        self.gnss_view_signal.connect(self.animate)
        self.gnss_view_signal.connect(self.init_gnss_draw)
        '''
        self.timer = QTimer()
        self.timer.timeout.connect(Nmea_Tcp.nmea)
        '''

    def connect_device_toggled_slot(self):
        if not self.connect_device.clicked():
            self.connect_device.setText("连接")
        else:
            self.connect_device.setText("断开连接")

    def connect_tcp(self):
        try:
            self.tcp_client_start("1.1.1.1", 15160)
        except:
            pass

    def rev_msg(self, msg):
        try:
            self.textEdit.append(msg)
        except:
            pass


if __name__ == "__main__":
    app = QApplication([])
    stats = UI_TOOL_UI()
    stats.show()
    app.exec()
