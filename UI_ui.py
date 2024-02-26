# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 730)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.General = QWidget()
        self.General.setObjectName(u"General")
        self.verticalLayout_12 = QVBoxLayout(self.General)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.General)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.LE_Path = QLineEdit(self.General)
        self.LE_Path.setObjectName(u"LE_Path")

        self.horizontalLayout_5.addWidget(self.LE_Path)

        self.BTN_Browse = QPushButton(self.General)
        self.BTN_Browse.setObjectName(u"BTN_Browse")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Browse.sizePolicy().hasHeightForWidth())
        self.BTN_Browse.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.BTN_Browse)

        self.TBTN_Reset_Path = QToolButton(self.General)
        self.TBTN_Reset_Path.setObjectName(u"TBTN_Reset_Path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TBTN_Reset_Path.sizePolicy().hasHeightForWidth())
        self.TBTN_Reset_Path.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.TBTN_Reset_Path)


        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.General)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.groupBox_3 = QGroupBox(self.General)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.RADIO_Head_Y = QRadioButton(self.groupBox_4)
        self.RADIO_Head_Y.setObjectName(u"RADIO_Head_Y")
        self.RADIO_Head_Y.setChecked(True)

        self.verticalLayout_2.addWidget(self.RADIO_Head_Y)

        self.RADIO_Head_N = QRadioButton(self.groupBox_4)
        self.RADIO_Head_N.setObjectName(u"RADIO_Head_N")

        self.verticalLayout_2.addWidget(self.RADIO_Head_N)


        self.verticalLayout_9.addWidget(self.groupBox_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.LE_Separator = QLineEdit(self.groupBox_3)
        self.LE_Separator.setObjectName(u"LE_Separator")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LE_Separator.sizePolicy().hasHeightForWidth())
        self.LE_Separator.setSizePolicy(sizePolicy2)
        self.LE_Separator.setBaseSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.LE_Separator, 0, Qt.AlignRight)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.SPINBOX_Column_w_Phone = QSpinBox(self.groupBox_3)
        self.SPINBOX_Column_w_Phone.setObjectName(u"SPINBOX_Column_w_Phone")
        self.SPINBOX_Column_w_Phone.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.SPINBOX_Column_w_Phone)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.Label_decode = QLabel(self.groupBox_3)
        self.Label_decode.setObjectName(u"Label_decode")

        self.horizontalLayout_8.addWidget(self.Label_decode)

        self.LE_decode = QLineEdit(self.groupBox_3)
        self.LE_decode.setObjectName(u"LE_decode")

        self.horizontalLayout_8.addWidget(self.LE_decode)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.RADIO_Insert_After_Phone = QRadioButton(self.groupBox_5)
        self.RADIO_Insert_After_Phone.setObjectName(u"RADIO_Insert_After_Phone")
        self.RADIO_Insert_After_Phone.setChecked(True)

        self.verticalLayout_4.addWidget(self.RADIO_Insert_After_Phone)

        self.RADIO_Insert_Last = QRadioButton(self.groupBox_5)
        self.RADIO_Insert_Last.setObjectName(u"RADIO_Insert_Last")

        self.verticalLayout_4.addWidget(self.RADIO_Insert_Last)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.RADIO_Insert_After = QRadioButton(self.groupBox_5)
        self.RADIO_Insert_After.setObjectName(u"RADIO_Insert_After")

        self.horizontalLayout.addWidget(self.RADIO_Insert_After)

        self.SPINBOX_Insert_After = QSpinBox(self.groupBox_5)
        self.SPINBOX_Insert_After.setObjectName(u"SPINBOX_Insert_After")
        self.SPINBOX_Insert_After.setMinimum(1)

        self.horizontalLayout.addWidget(self.SPINBOX_Insert_After)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.groupBox_8 = QGroupBox(self.groupBox_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.RADIO_Phone_As_Source = QRadioButton(self.groupBox_8)
        self.RADIO_Phone_As_Source.setObjectName(u"RADIO_Phone_As_Source")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.RADIO_Phone_As_Source.sizePolicy().hasHeightForWidth())
        self.RADIO_Phone_As_Source.setSizePolicy(sizePolicy3)
        self.RADIO_Phone_As_Source.setChecked(True)

        self.verticalLayout_6.addWidget(self.RADIO_Phone_As_Source)

        self.RADIO_Phone_7x = QRadioButton(self.groupBox_8)
        self.RADIO_Phone_7x.setObjectName(u"RADIO_Phone_7x")
        sizePolicy3.setHeightForWidth(self.RADIO_Phone_7x.sizePolicy().hasHeightForWidth())
        self.RADIO_Phone_7x.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.RADIO_Phone_7x)

        self.RADIO_Phone_Plus7x = QRadioButton(self.groupBox_8)
        self.RADIO_Phone_Plus7x.setObjectName(u"RADIO_Phone_Plus7x")
        sizePolicy3.setHeightForWidth(self.RADIO_Phone_Plus7x.sizePolicy().hasHeightForWidth())
        self.RADIO_Phone_Plus7x.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.RADIO_Phone_Plus7x)

        self.RADIO_Phone_8x = QRadioButton(self.groupBox_8)
        self.RADIO_Phone_8x.setObjectName(u"RADIO_Phone_8x")
        sizePolicy3.setHeightForWidth(self.RADIO_Phone_8x.sizePolicy().hasHeightForWidth())
        self.RADIO_Phone_8x.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.RADIO_Phone_8x)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout_8.addWidget(self.groupBox_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.line_4 = QFrame(self.groupBox_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.RADIO_Selected_Regions = QRadioButton(self.groupBox_6)
        self.RADIO_Selected_Regions.setObjectName(u"RADIO_Selected_Regions")
        self.RADIO_Selected_Regions.setChecked(True)

        self.verticalLayout_3.addWidget(self.RADIO_Selected_Regions)

        self.RADIO_All_Regions = QRadioButton(self.groupBox_6)
        self.RADIO_All_Regions.setObjectName(u"RADIO_All_Regions")

        self.verticalLayout_3.addWidget(self.RADIO_All_Regions)


        self.verticalLayout_7.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.RADIO_XLSX = QRadioButton(self.groupBox_7)
        self.RADIO_XLSX.setObjectName(u"RADIO_XLSX")
        self.RADIO_XLSX.setChecked(True)

        self.verticalLayout_5.addWidget(self.RADIO_XLSX)

        self.RADIO_CSV = QRadioButton(self.groupBox_7)
        self.RADIO_CSV.setObjectName(u"RADIO_CSV")

        self.verticalLayout_5.addWidget(self.RADIO_CSV)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.CB_Separator_to_Save = QComboBox(self.groupBox_7)
        self.CB_Separator_to_Save.addItem("")
        self.CB_Separator_to_Save.addItem("")
        self.CB_Separator_to_Save.addItem("")
        self.CB_Separator_to_Save.setObjectName(u"CB_Separator_to_Save")
        sizePolicy2.setHeightForWidth(self.CB_Separator_to_Save.sizePolicy().hasHeightForWidth())
        self.CB_Separator_to_Save.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.CB_Separator_to_Save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addWidget(self.groupBox_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.line_3 = QFrame(self.General)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_13 = QLabel(self.General)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_10.addWidget(self.label_13)

        self.LW_All_Regions = QListWidget(self.General)
        self.LW_All_Regions.setObjectName(u"LW_All_Regions")

        self.verticalLayout_10.addWidget(self.LW_All_Regions)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.General)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_11.addWidget(self.label_14)

        self.LW_Selected_Regions = QListWidget(self.General)
        self.LW_Selected_Regions.setObjectName(u"LW_Selected_Regions")

        self.verticalLayout_11.addWidget(self.LW_Selected_Regions)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.BTN_Render = QPushButton(self.General)
        self.BTN_Render.setObjectName(u"BTN_Render")
        self.BTN_Render.setEnabled(False)

        self.verticalLayout_12.addWidget(self.BTN_Render)

        self.tabWidget.addTab(self.General, "")
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.groupBox = QGroupBox(self.Settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 250, 871, 211))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 161, 21))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 211, 31))
        self.CB_interval_Upd_NE = QComboBox(self.groupBox)
        self.CB_interval_Upd_NE.addItem("")
        self.CB_interval_Upd_NE.addItem("")
        self.CB_interval_Upd_NE.addItem("")
        self.CB_interval_Upd_NE.addItem("")
        self.CB_interval_Upd_NE.setObjectName(u"CB_interval_Upd_NE")
        self.CB_interval_Upd_NE.setGeometry(QRect(240, 110, 171, 22))
        self.LE_Link_Download_Upd = QLineEdit(self.groupBox)
        self.LE_Link_Download_Upd.setObjectName(u"LE_Link_Download_Upd")
        self.LE_Link_Download_Upd.setGeometry(QRect(180, 60, 551, 20))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 291, 21))
        self.CB_Mode_Upd_NE = QComboBox(self.groupBox)
        self.CB_Mode_Upd_NE.addItem("")
        self.CB_Mode_Upd_NE.addItem("")
        self.CB_Mode_Upd_NE.setObjectName(u"CB_Mode_Upd_NE")
        self.CB_Mode_Upd_NE.setGeometry(QRect(320, 30, 251, 22))
        self.BTN_reset_Link_Download_Upd = QToolButton(self.groupBox)
        self.BTN_reset_Link_Download_Upd.setObjectName(u"BTN_reset_Link_Download_Upd")
        self.BTN_reset_Link_Download_Upd.setGeometry(QRect(770, 60, 51, 21))
        self.BTN_Upd_Now_NE = QPushButton(self.groupBox)
        self.BTN_Upd_Now_NE.setObjectName(u"BTN_Upd_Now_NE")
        self.BTN_Upd_Now_NE.setGeometry(QRect(20, 150, 181, 21))
        self.LABEL_Actuality_Version_NE = QLabel(self.groupBox)
        self.LABEL_Actuality_Version_NE.setObjectName(u"LABEL_Actuality_Version_NE")
        self.LABEL_Actuality_Version_NE.setGeometry(QRect(220, 160, 321, 21))
        self.groupBox_2 = QGroupBox(self.Settings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 20, 801, 181))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 211, 31))
        self.CB_interval_Upd_PO = QComboBox(self.groupBox_2)
        self.CB_interval_Upd_PO.addItem("")
        self.CB_interval_Upd_PO.addItem("")
        self.CB_interval_Upd_PO.addItem("")
        self.CB_interval_Upd_PO.setObjectName(u"CB_interval_Upd_PO")
        self.CB_interval_Upd_PO.setGeometry(QRect(220, 40, 171, 22))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 181, 21))
        self.CB_Mode_Upd_PO = QComboBox(self.groupBox_2)
        self.CB_Mode_Upd_PO.addItem("")
        self.CB_Mode_Upd_PO.addItem("")
        self.CB_Mode_Upd_PO.setObjectName(u"CB_Mode_Upd_PO")
        self.CB_Mode_Upd_PO.setGeometry(QRect(180, 70, 251, 22))
        self.BTN_Upd_Now_PO = QPushButton(self.groupBox_2)
        self.BTN_Upd_Now_PO.setObjectName(u"BTN_Upd_Now_PO")
        self.BTN_Upd_Now_PO.setGeometry(QRect(10, 110, 181, 21))
        self.LABEL_Actuality_Version_PO = QLabel(self.groupBox_2)
        self.LABEL_Actuality_Version_PO.setObjectName(u"LABEL_Actuality_Version_PO")
        self.LABEL_Actuality_Version_PO.setGeometry(QRect(210, 110, 231, 21))
        self.pushButton = QPushButton(self.Settings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 630, 81, 31))
        self.pushButton_2 = QPushButton(self.Settings)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(500, 630, 171, 31))
        self.tabWidget.addTab(self.Settings, "")
        self.About = QWidget()
        self.About.setObjectName(u"About")
        self.label_6 = QLabel(self.About)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 20, 81, 21))
        self.label_7 = QLabel(self.About)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(125, 26, 35, 10))
        self.label_8 = QLabel(self.About)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(160, 23, 131, 16))
        self.tabWidget.addTab(self.About, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0435\u043c\u044b\u0435 \u0444\u043e\u0440\u043c\u0430\u0442\u044b CSV, XLS, XLSX, TXT", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u0441 \u043d\u043e\u043c\u0435\u0440\u0430\u043c\u0438 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043e\u0432:", None))
        self.BTN_Browse.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.TBTN_Reset_Path.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0430 \u0441 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c:", None))
        self.RADIO_Head_Y.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u0442\u044c", None))
        self.RADIO_Head_N.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c:", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u043e\u043b\u043e\u043d\u043a\u0438 \u043f\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0443 \u0432 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u043d\u0430\u0445\u043e\u0434\u044f\u0442\u0441\u044f \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0435 \u043d\u043e\u043c\u0435\u0440\u0430 ", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u2116 \u043a\u043e\u043b\u043e\u043d\u043a\u0438 \u0441 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430\u043c\u0438:", None))
        self.Label_decode.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434\u0438\u0440\u043e\u0432\u043a\u0430 \u0444\u0430\u0439\u043b\u0430:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043d\u043e\u043c\u0435\u0440\u0435 \u043f\u043e\u0441\u043b\u0435:", None))
        self.RADIO_Insert_After_Phone.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0438 \u0441 \u043d\u043e\u043c\u0435\u0440\u043e\u043c \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.RADIO_Insert_Last.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0445 \u043a\u043e\u043b\u043e\u043d\u043e\u043a", None))
        self.RADIO_Insert_After.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043d\u043a\u0438 \u2116", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442:", None))
        self.RADIO_Phone_As_Source.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u043a \u0432 \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u043c", None))
        self.RADIO_Phone_7x.setText(QCoreApplication.translate("MainWindow", u"7xxxxxxxxxx", None))
        self.RADIO_Phone_Plus7x.setText(QCoreApplication.translate("MainWindow", u"+7xxxxxxxxxx", None))
        self.RADIO_Phone_8x.setText(QCoreApplication.translate("MainWindow", u"8xxxxxxxxxx", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430:", None))
        self.RADIO_Selected_Regions.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0438\u0437 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0440\u0435\u0433\u0438\u043e\u043d\u0430", None))
        self.RADIO_All_Regions.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0440\u0435\u0433\u0438\u043e\u043d\u044b", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0440\u043c\u0430\u0442 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0444\u0430\u0439\u043b\u0430:", None))
        self.RADIO_XLSX.setText(QCoreApplication.translate("MainWindow", u"XLSX", None))
        self.RADIO_CSV.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c:", None))
        self.CB_Separator_to_Save.setItemText(0, QCoreApplication.translate("MainWindow", u";", None))
        self.CB_Separator_to_Save.setItemText(1, QCoreApplication.translate("MainWindow", u",", None))
        self.CB_Separator_to_Save.setItemText(2, QCoreApplication.translate("MainWindow", u":", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d\u044b (\u0434\u0432\u043e\u0439\u043d\u043e\u0439 \u043a\u043b\u0438\u043a \u0434\u043b\u044f \u0432\u044b\u0431\u043e\u0440\u0430):", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0440\u0435\u0433\u0438\u043e\u043d\u044b (\u0434\u0432\u043e\u0439\u043d\u043e\u0439 \u043a\u043b\u0438\u043a \u0434\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f):", None))
        self.BTN_Render.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440\u043d\u044b\u0435 \u0451\u043c\u043a\u043e\u0441\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u0434\u043b\u044f \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043a\u0430\u0436\u0434\u044b\u0435", None))
        self.CB_interval_Upd_NE.setItemText(0, QCoreApplication.translate("MainWindow", u"7 \u0434\u043d\u0435\u0439", None))
        self.CB_interval_Upd_NE.setItemText(1, QCoreApplication.translate("MainWindow", u"30 \u0434\u043d\u0435\u0439", None))
        self.CB_interval_Upd_NE.setItemText(2, QCoreApplication.translate("MainWindow", u"90 \u0434\u043d\u0435\u0439", None))
        self.CB_interval_Upd_NE.setItemText(3, QCoreApplication.translate("MainWindow", u"180 \u0434\u043d\u0435\u0439", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0435 \u043d\u043e\u043c\u0435\u0440\u043d\u044b\u0435 \u0451\u043c\u043a\u043e\u0441\u0442\u0438 \u0441\u043a\u0430\u0447\u0438\u0432\u0430\u0442\u044c ", None))
        self.CB_Mode_Upd_NE.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.CB_Mode_Upd_NE.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))

        self.BTN_reset_Link_Download_Upd.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.BTN_Upd_Now_NE.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.LABEL_Actuality_Version_NE.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0435 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0435 \u043d\u043e\u043c\u0435\u0440\u043d\u044b\u0435 \u0451\u043c\u043a\u043e\u0441\u0442\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044f\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043a\u0430\u0436\u0434\u044b\u0435", None))
        self.CB_interval_Upd_PO.setItemText(0, QCoreApplication.translate("MainWindow", u"30 \u0434\u043d\u0435\u0439", None))
        self.CB_interval_Upd_PO.setItemText(1, QCoreApplication.translate("MainWindow", u"90 \u0434\u043d\u0435\u0439", None))
        self.CB_interval_Upd_PO.setItemText(2, QCoreApplication.translate("MainWindow", u"180 \u0434\u043d\u0435\u0439", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0438\u0432\u0430\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.CB_Mode_Upd_PO.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.CB_Mode_Upd_PO.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))

        self.BTN_Upd_Now_PO.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.LABEL_Actuality_Version_PO.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0435 \u0430\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u0443\u044e \u0432\u0435\u0440\u0441\u0438\u044e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0441\u0438\u044f \u041f\u041e:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"(\u043f\u043e\u0441\u043b\u0435\u0434\u043d\u044f\u044f)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

