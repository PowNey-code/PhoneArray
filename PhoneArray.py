# проверить размер файла на сервере
import urllib.request
from params import P, Params
import Update as upd
from datetime import datetime, date
import time
import os
import sys
# from PySide6 import QtGui
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader


#! Надо проверить есть ли файлы вообще
prm = Params()

# upd.Check_Arrays()
# different_date = abs((date.today() - prm.last_Update).days)
# if different_date >= prm.frequency:
#     upd.Check_Update_Arrays()


if __name__ == "__main__":

Qt::AA_ShareOpenGLContexts using QCoreApplication::setAttribute and QSGRendererInterface::OpenGLRhi using QQuickWindow::setGraphicsApi


    app = QApplication(sys.argv)
    ui_file_name = "UI.ui"
    ui_file = QFile(ui_file_name)
    # if not ui_file.open(QIODevice.ReadOnly):
    #     print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
    #     sys.exit(-1)
    loader = QUiLoader()
    w = loader.load(ui_file)
    ui_file.close()
    # if not w:
    #     print(loader.errorString())
    #     sys.exit(-1)
    w.show()

    sys.exit(app.exec())










# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     w = UI()
#     w.show()
#     sys.exit(app.exec())