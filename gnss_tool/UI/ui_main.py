# coding=utf-8

################################################################################
## Form generated from reading UI file 'gnss.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMdiArea, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actiongnss_view = QAction(MainWindow)
        self.actiongnss_view.setObjectName(u"actiongnss_view")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gnss_view_2 = QTabWidget(self.centralwidget)
        self.gnss_view_2.setObjectName(u"gnss_view_2")
        self.gnss_view_2.setGeometry(QRect(0, 0, 801, 800))
        self.gnss_view_2.setMinimumSize(QSize(0, 800))
        self.gnss_view = QWidget()
        self.gnss_view.setObjectName(u"gnss_view")
        self.mdiArea = QMdiArea(self.gnss_view)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(280, 90, 511, 431))
        self.layoutWidget = QWidget(self.gnss_view)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 271, 521))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.ip_or_com = QLineEdit(self.layoutWidget)
        self.ip_or_com.setObjectName(u"ip_or_com")

        self.gridLayout.addWidget(self.ip_or_com, 1, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.connect_type = QComboBox(self.layoutWidget)
        self.connect_type.addItem("")
        self.connect_type.addItem("")
        self.connect_type.addItem("")
        self.connect_type.addItem("")
        self.connect_type.setObjectName(u"connect_type")

        self.gridLayout.addWidget(self.connect_type, 0, 3, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.connect_device = QCheckBox(self.layoutWidget)
        self.connect_device.setObjectName(u"connect_device")

        self.verticalLayout_3.addWidget(self.connect_device)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cleardata = QPushButton(self.layoutWidget)
        self.cleardata.setObjectName(u"cleardata")
        sizePolicy.setHeightForWidth(self.cleardata.sizePolicy().hasHeightForWidth())
        self.cleardata.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.cleardata)

        self.savedata = QPushButton(self.layoutWidget)
        self.savedata.setObjectName(u"savedata")

        self.horizontalLayout_4.addWidget(self.savedata)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.button_5 = QPushButton(self.layoutWidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setTabletTracking(False)
        self.button_5.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout.addWidget(self.button_5)

        self.button_4 = QPushButton(self.layoutWidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setTabletTracking(False)
        self.button_4.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout.addWidget(self.button_4)

        self.data_analy = QCheckBox(self.layoutWidget)
        self.data_analy.setObjectName(u"data_analy")

        self.verticalLayout.addWidget(self.data_analy)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setUndoRedoEnabled(False)

        self.verticalLayout_2.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.gnss_view_2.addTab(self.gnss_view, "")
        self.gnss_data = QWidget()
        self.gnss_data.setObjectName(u"gnss_data")
        self.gnss_view_2.addTab(self.gnss_data, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actiongnss_view)

        self.retranslateUi(MainWindow)

        self.gnss_view_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiongnss_view.setText(QCoreApplication.translate("MainWindow", u"gnss_view", None))
#if QT_CONFIG(whatsthis)
        self.gnss_view_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a", None))
        self.connect_type.setItemText(0, QCoreApplication.translate("MainWindow", u"TCP\u5ba2\u6237\u7aef", None))
        self.connect_type.setItemText(1, QCoreApplication.translate("MainWindow", u"TCP\u670d\u52a1\u7aef", None))
        self.connect_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))
        self.connect_type.setItemText(3, QCoreApplication.translate("MainWindow", u"NtripClient", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP/\u4e32\u53e3\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65b9\u5f0f\uff1a", None))
        self.connect_device.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.cleardata.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6570\u636e", None))
        self.savedata.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6570\u636e", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bfb\u53d6", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8bfb\u53d6", None))
        self.data_analy.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u6570\u636e", None))
        self.gnss_view_2.setTabText(self.gnss_view_2.indexOf(self.gnss_view), QCoreApplication.translate("MainWindow", u"gnss_view", None))
        self.gnss_view_2.setTabText(self.gnss_view_2.indexOf(self.gnss_data), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5904\u7406", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e38\u7528\u5de5\u5177", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5206\u6790", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi
