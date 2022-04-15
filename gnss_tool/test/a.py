from PySide6.QtWidgets import QApplication, QTabWidget, QPushButton

app = QApplication()
tabwidget = QTabWidget()
tabwidget.addTab(QPushButton('tab1'), 'tab1')
tabwidget.addTab(QPushButton('tab2'), 'tab2')
tabwidget.show()
app.exec()