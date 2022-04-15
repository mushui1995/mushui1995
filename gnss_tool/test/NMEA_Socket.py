# coding=utf-8
import socket
import os
import math
import time

from PySide6.QtCore import QTimer
from gnss_tool.UI.ui_main import Ui_MainWindow


class Nmea_Tcp(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Ui_MainWindow.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def nmea_tcp_connect(self, ip, com):
        self.s.connect((ip, com))

    def nmea(self):
        while self.connect_device.isChecked():
            data = self.s.recv(4096)
            D = str(data).split(r"\r\n")
            for d in D:
                if d == "'":
                    pass
                elif d.startswith("b'"):
                    print((d + ',\n')[2:])
                    self.textEdit.setText((d + ',\n')[2:])
                else:
                    self.textEdit.setText(d + ',\n')
                textCursor = self.textEdit.textCursor()
                # 滚动到底部
                textCursor.movePosition(textCursor.End)
                # 设置光标到text中去
                self.textEdit.setTextCursor(textCursor)

    def nmea_tcp_disconnect(self):
        self.s.close()
