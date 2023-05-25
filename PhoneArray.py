# проверить размер файла на сервере
import urllib.request
from params import P, Params
import Update as upd
from MakeClassFromUI import ClassFromUI
from datetime import datetime, date
import time
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QCoreApplication, Qt


#! Надо проверить есть ли файлы вообще
prm = Params()
# upd.Check_Arrays()
# different_date = abs((date.today() - prm.last_Update).days)
# if different_date >= prm.frequency:
#     upd.Check_Update_Arrays()



ClassUI = ClassFromUI(P + 'UI.ui')
class UI(QMainWindow, ClassUI):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)

        self.LE_Path.setText('ddddd')
        self.LE_Separator.setText(';')
        
        self.show()

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    Window = UI()
    sys.exit(app.exec())
