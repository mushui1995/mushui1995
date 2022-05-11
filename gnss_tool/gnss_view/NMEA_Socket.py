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
    gnss_view_signal = Signal(dict)

    def __init__(self):
        super().__init__()

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
            GPGSV_list, GLGSV_list, GAGSV_list, BDGSV_list = [], [], [], []
            gpgsv_num_i, gagsv_num_i, glgsv_num_i, bdgsv_num_i = 0, 0, 0, 0
            if data:
                D = str(data).split(r"\r\n")
                for d in D:
                    msg = ""
                    if d == "'":
                        pass
                    elif d.startswith("b'"):
                        msg = (d + ',\n')[2:]  # 提起NMEA数据
                        self.tcp_rev_msg_signal.emit(msg)
                    else:
                        msg = (d + ',\n')
                        self.tcp_rev_msg_signal.emit(msg)

                    '''
                    后续为NMEA数据处理
                    '''
                    if len(msg) > 5:

                        msg_list = msg.split(",")
                        if msg_list[0] == "$GPGSV" and len(msg_list) > 7 and len(msg_list[-2]) > 2:
                            gpsgsv_len = len(msg_list)
                            if int(msg_list[2]) != gpgsv_num_i:  #
                                sat_num = int((gpsgsv_len - 5) / 4)
                                for i in range(0, sat_num):
                                    j = (i + 1) * 4
                                    if msg_list[j] != '' and "*" not in msg_list[j + 3][:2]:  # 判断内容不为空
                                        GPGSV_list.append(
                                            [msg_list[j], msg_list[j + 1], msg_list[j + 2], msg_list[j + 3][:2]])
                                gpgsv_num_i = int(msg_list[2])  # 卫星数量
                        elif msg_list[0] == "$GAGSV" and len(msg_list) > 7 and len(msg_list[-2]) > 2:
                            gagsv_len = len(msg_list)
                            if int(msg_list[2]) != gagsv_num_i:  #
                                sat_num = int((gagsv_len - 5) / 4)
                                for i in range(0, sat_num):
                                    j = (i + 1) * 4
                                    if msg_list[j] != '' and "*" not in msg_list[j + 3][:2]:  # 判断内容不为空
                                        GAGSV_list.append(
                                            [msg_list[j], msg_list[j + 1], msg_list[j + 2], msg_list[j + 3][:2]])
                                gagsv_num_i = int(msg_list[2])
                        elif msg_list[0] == "$GLGSV" and len(msg_list) > 7 and len(msg_list[-2]) > 2:
                            glgsv_len = len(msg_list)
                            if int(msg_list[2]) != glgsv_num_i:  #
                                sat_num = int((glgsv_len - 5) / 4)
                                for i in range(0, sat_num):
                                    j = (i + 1) * 4
                                    if msg_list[j] != '' and "*" not in msg_list[j + 3][:2]:  # 判断内容不为空
                                        GLGSV_list.append(
                                            [msg_list[j], msg_list[j + 1], msg_list[j + 2], msg_list[j + 3][:2]])
                                glgsv_num_i = int(msg_list[2])
                        elif msg_list[0] == "$BDGSV" and len(msg_list) > 7 and len(msg_list[-2]) > 2:
                            bdgsv_len = len(msg_list)
                            if int(msg_list[2]) != bdgsv_num_i:  #
                                sat_num = int((bdgsv_len - 5) / 4)
                                for i in range(0, sat_num):
                                    j = (i + 1) * 4
                                    if msg_list[j] != '' and "*" not in msg_list[j + 3][:2]:  # 判断内容不为空
                                        BDGSV_list.append(
                                            [msg_list[j], msg_list[j + 1], msg_list[j + 2], msg_list[j + 3][:2]])
                                bdgsv_num_i = int(msg_list[2])
                if len(GPGSV_list) != 0 or len(GAGSV_list) != 0 or len(GLGSV_list) != 0 or len(BDGSV_list) != 0:
                    gnss_signal = dict(
                        zip(["GPS", "GAL", "GLO", "BDS", ], [GPGSV_list, GAGSV_list, GLGSV_list, BDGSV_list]))
                    self.gnss_view_signal.emit(gnss_signal)

            else:
                self.s.close()
                msg = "服务器连接断开..."
                self.tcp_rev_msg_signal.emit(msg)
                break

    def nmea_tcp_disconnect(self):
        self.s.close()
