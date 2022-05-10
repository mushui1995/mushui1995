# coding=utf-8
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from NMEA_Socket import Nmea_Tcp
from gnss_tool.UI.ui_mian import Ui_MainWindow
import os


class GNSS_TOOL_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GNSS_TOOL_UI, self).__init__(parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init()

    def init(self):
        connect_device = self.connect_device
        connect_device.setChecked(False)
        connect_device.stateChanged.connect(lambda: self.check_box_connect())
        connect_device.stateChanged.connect(lambda: self.nmea())
        '''
        self.timer = QTimer()
        self.timer.timeout.connect(Nmea_Tcp.nmea)'''

    def check_box_connect(self):
        if self.connect_device.isChecked():
            Nmea_Tcp().nmea_tcp_connect("1.1.1.1", 15160)
        else:
            Nmea_Tcp().nmea_tcp_disconnect()

    def nmea(self):
        if self.connect_device.isChecked():
            print("con")
            Nmea_Tcp().nmea()
        else:
            print("dis")


if __name__ == "__main__":
    app = QApplication([])
    stats = GNSS_TOOL_UI()
    stats.show()
    app.exec()
