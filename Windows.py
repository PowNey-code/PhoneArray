from params import P, Params
import fn
import time
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon, QPixmap


class ProgressWin(QDialog):
    def __init__(self, Title:str, MaxCount:int, H1:str='', Descr:str='$$'):
        super(ProgressWin, self).__init__()
        self.setModal(True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)
        self.setWindowIcon(QIcon(P + 'img\\loader.png'))

        self.setWindowTitle(Title)

        self.CurrentI = 0
        self.MaxCount = MaxCount
        self.Descr = Descr

        self.Vlayout = QVBoxLayout(self)
        self.VSpacer = QSpacerItem(20, 15, QSizePolicy.Expanding)

        self.Label_H1 = QLabel(H1)
        self.Label_H1.setFont(QFont('Verdana', 10))
        self.Vlayout.addWidget(self.Label_H1)

        self.Vlayout.addItem(self.VSpacer)

        self.Label_Descr = QLabel(alignment = Qt.AlignHCenter)
        self.Label_Descr.setFont(QFont('Verdana', 10))
        self.Vlayout.addWidget(self.Label_Descr)

        self.ProgressBar = QProgressBar()
        self.Vlayout.addWidget(self.ProgressBar)
        self.setPrcnt(0)

        self.show()


    def setDescr(self, text:str, style=None):
        self.Label_Descr.setText(text)
        if style is None:
            self.Label_Descr.setStyleSheet("color: black;")
        else:
            self.Label_Descr.setStyleSheet(style)

    
    def setMaxCount(self, MaxCount:int):
        self.MaxCount = MaxCount
        self.setPrcnt(self.CurrentI)


    def setPrcnt(self, CurrentI:int):
        self.CurrentI = CurrentI
        prcnt = ( CurrentI / self.MaxCount ) * 100
        prcnt = int(prcnt)

        tmp = f'{fn.format_digit(CurrentI/1024)} / {fn.format_digit(self.MaxCount/1024)}'
        text = self.Descr.replace('$$', tmp)

        self.Label_Descr.setText(text)
        self.ProgressBar.setValue(prcnt)
        if CurrentI >= self.MaxCount:
            time.sleep(1)
            self.close()


    def __call__(self, CurrentI:int):
        self.setPrcnt(CurrentI)


class MessageWin(QDialog):
    def __init__(self, Title:str, Type:str, Descr:str):
        super(ProgressWin, self).__init__()
        self.setModal(True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)

        self.setWindowTitle(Title)

        if Type == 'error':
            self.setWindowIcon(QIcon(P + 'img\\error.png'))
            self.pixmap = QPixmap(P + 'img\\error.png')
            self.btn = QPushButton('Закрыть программу', default=True)
        else:
            self.setWindowIcon(QIcon(P + 'img\\ok.png'))
            self.pixmap = QPixmap(P + 'img\\ok.png')
            self.btn = QPushButton('Хорошо', default=True)

        self.Hlayout = QHBoxLayout(self)


        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(self.pixmap)
        self.resize(self.pixmap.width(), self.pixmap.height())
        self.Hlayout.addWidget(self.imgLabel)

        self.Label_Descr = QLabel(text = Descr, alignment = Qt.AlignHCenter)
        self.Label_Descr.setFont(QFont('Verdana', 10))
        self.Hlayout.addWidget(self.Label_Descr)




        self.Vlayout = QVBoxLayout(self)
        self.Vlayout.addLayout(self.Hlayout)

        self.VSpacer = QSpacerItem(20, 15, QSizePolicy.Expanding)
        self.Vlayout.addItem(self.VSpacer)

        self.Vlayout.addItem(self.btn)


        self.show()