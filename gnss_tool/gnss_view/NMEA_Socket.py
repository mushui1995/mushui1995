# coding=utf-8
import socket
import os
import math
import time
import threading
from PySide6.QtCore import QTimer, Signal
from gnss_tool.UI.ui_main import Ui_MainWindow


class Nmea_Tcp(Ui_MainWindow):
    tcp_rev_msg_signal = Signal(str)

    def __init__(self):
        super().__init__()
        # Ui_MainWindow.__init__(self)

    def tcp_client_start(self, ip: str, port: int):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        adress = (ip, port)
        try:
            self.s.connect(adress)
        except:
            msg = "连接不上服务器...\n"
            self.tcp_rev_msg_signal.emit(msg)
        else:
            self.tcp_client_msg = threading.Thread(target=self.nmea)
            self.tcp_client_msg.start()
            msg = "服务器已连接成功..."
            self.tcp_rev_msg_signal.emit(msg)

    def nmea(self):
        while True:
            data = self.s.recv(4096)
            if data:
                D = str(data).split(r"\r\n")
                for d in D:
                    if d == "'":
                        pass
                    elif d.startswith("b'"):
                        msg = (d + ',\n')[2:]
                        self.tcp_rev_msg_signal.emit(msg)
                    else:
                        msg = (d + ',\n')
                        self.tcp_rev_msg_signal.emit(msg)
            else:
                self.s.close()
                msg = "服务器连接断开..."
                self.tcp_rev_msg_signal.emit(msg)
                break

    def nmea_tcp_disconnect(self):
        self.s.close()
