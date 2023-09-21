from params import P, Params
import math
from PySide6.QtWidgets import QDialog, QStyle, QVBoxLayout, QHBoxLayout, QLabel, QProgressBar, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon


class PW(QDialog):
    def __init__(self, Title, MaxCount, H1='', Descr=''):
        super(PW, self).__init__()
        self.setModal(True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)
        self.setWindowIcon(QIcon(P + 'img\\loader.png'))

        self.setWindowTitle(Title)

        self.CurrentI = 0
        self.MaxCount = MaxCount

        self.Vlayout = QVBoxLayout(self)
        self.VSpacer = QSpacerItem(20, 15, QSizePolicy.Expanding)

        self.Label_H1 = QLabel(H1)
        self.Label_H1.setFont(QFont('Verdana', 10))
        self.Vlayout.addWidget(self.Label_H1)

        self.Vlayout.addItem(self.VSpacer)

        # self.Label_Descr = QLabel(Descr, alignment = Qt.AlignHCenter)
        self.Label_Descr = QLabel(alignment = Qt.AlignHCenter)
        self.Label_Descr.setFont(QFont('Verdana', 10))
        self.Vlayout.addWidget(self.Label_Descr)

        self.ProgressBar = QProgressBar()
        self.ProgressBar.setValue(0)
        self.Vlayout.addWidget(self.ProgressBar)

        self.show()


    def setDescr(self, text, style=None):
        self.Label_Descr.setText(text)
        if style is None:
            self.Label_Descr.setStyleSheet("color: black;")
        else:
            self.Label_Descr.setStyleSheet(style)

    
    def setMaxCount(self, MaxCount):
        self.MaxCount = MaxCount
        self.setPrcnt(self.CurrentI)


    def setPrcnt(self, CurrentI):
        self.CurrentI = CurrentI
        prcnt = CurrentI / self.MaxCount
        prcnt = math.floor(prcnt * 100)
        self.ProgressBar.setValue(prcnt)


    def __call__(self, CurrentI):
        self.setPrcnt(CurrentI)