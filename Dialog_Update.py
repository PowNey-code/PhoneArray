from params import P, Params
# import fn
import ProgressWindow as PW
# import os
from PySide6.QtWidgets import QDialog, QStyle, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont
prm = Params()

class Update_Ask(QDialog):
    def __init__(self, MainWindow, bases):
        super(Update_Ask, self).__init__()
        
        self.setModal(True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_BrowserReload))
        self.setWindowFlags(Qt.WindowSystemMenuHint)
        self.setWindowTitle('Обновление номерных ёмкостей')
        # self.resize(250, 200)

        self.MainWindow = MainWindow
        self.bases = bases
        print(bases)

        if type(bases) == dict:
            # Если некоторые файлы отсутствуют и возможно некоторые нужно обновить
            if any([bases[f]['status'] == 'no_file' for f in bases]):
                # Если некоторые файлы отсутствуют и некоторые нужно обновить
                if any([bases[f]['status'] == 'old' for f in bases]):
                    mess = f"Некоторые файлы с номерной ёмкостью отсутствуют(без них работа не возможна), а некоторые устарели.<br>Скачать недостающие и обновить устаревшие файлы?"
                    self.btn_positiv = QPushButton('Скачать и обновить все', default=True)
                    self.btn_neutral = QPushButton("Скачать только недостающие", autoDefault=False)
                    self.btn_neutral.setFont(QFont('Verdana', 11))
                    self.btn_negativ = QPushButton('Завершить работу программы', autoDefault=False)

                    # self.btn_positiv.clicked.connect(self.Update)
                    self.btn_positiv.clicked.connect(lambda: self.Update(how='all'))
                    self.btn_neutral.clicked.connect(lambda:self.Update(how='no_files'))
                    self.btn_negativ.clicked.connect(self.closeProgram)

                # Если некоторые файлы отсутствуют
                else:
                    mess = f"Некоторые файлы с номерной ёмкостью отсутствуют, без них работа не возможна.<br>Скачать недостающие файлы?"
                    self.btn_positiv = QPushButton('Скачать', default=True)
                    self.btn_negativ = QPushButton('Завершить работу программы', autoDefault=False)

                    # self.btn_positiv.clicked.connect(self.Update)
                    self.btn_positiv.clicked.connect(lambda: self.Update(how='all'))
                    self.btn_negativ.clicked.connect(self.closeProgram)

            # Если все файлы найдены но нуждаются в обновлении
            else:
                for i, file in enumerate(bases, start = 0):
                    if i == 0:
                        newest_date = bases[file]['server_date']
                        oldest_date = bases[file]['local_date']

                    if oldest_date > bases[file]['local_date']:
                        oldest_date = bases[file]['local_date']

                    if newest_date < bases[file]['server_date']:
                        newest_date = bases[file]['server_date']

                mess = f"Доступны новые версии номерных ёмкостей (<span style='color:green'>{newest_date.strftime('%d.%m.%Y')}</span>), сейчас установленны <span style='color:red'>{oldest_date.strftime('%d.%m.%Y')}</span>.<br>Скачать обновления?"
                self.btn_positiv = QPushButton('Обновить', default=True)
                self.btn_negativ = QPushButton('Напомнить следующий раз', autoDefault=False)

                # self.btn_positiv.clicked.connect(self.Update)
                self.btn_positiv.clicked.connect(lambda: self.Update(how='all'))
                self.btn_negativ.clicked.connect(self.closeWindow)

        # Если папка папка с номерной ёмкостью не обнаружена
        else:
            mess = f"Директория содержащая номерную ёмкость ({P}{prm()['Auto_Update']['folder']}) не обнаружена, без неё работа не возможна.<br>Скачать номерную ёмкость?"
            self.btn_positiv = QPushButton('Скачать', default=True)
            self.btn_negativ = QPushButton('Завершить работу программы', autoDefault=False)

            # self.btn_positiv.clicked.connect(self.Update)
            self.btn_positiv.clicked.connect(lambda: self.Update(how='all'))
            self.btn_negativ.clicked.connect(self.closeProgram)


        self.Answer = QLabel(mess)
        self.Answer.setFont(QFont('Verdana', 10))

        self.btn_positiv.setFont(QFont('Verdana', 11))
        self.btn_positiv.setStyleSheet("color: green; padding: 6 15;")

        self.btn_negativ.setFont(QFont('Verdana', 11))
        self.btn_negativ.setStyleSheet("color: red; padding: 6 15;")


        self.Hlayout = QHBoxLayout()
        self.Hlayout.addWidget(self.btn_positiv)
        if hasattr(self, 'btn_neutral'):
            self.Hlayout.addWidget(self.btn_neutral)
        self.Hlayout.addWidget(self.btn_negativ)

        self.Vlayout = QVBoxLayout(self)
        self.Vlayout.addWidget(self.Answer)
        
        self.VSpacer = QSpacerItem(20, 15, QSizePolicy.Expanding)
        self.Vlayout.addItem(self.VSpacer)
        self.Vlayout.addLayout(self.Hlayout)
    
        self.show()
        # btn_update_all.clicked.connect(lambda: MainWindow.dialog_report(question='y', SenderName='direction'))


    def Update(self, how:str):
        total_size = 0
        if how != 'all':
            bases = {}
            for f in self.bases:
                if self.bases[f]['status'] == 'no_file':
                    bases[f] = self.bases[f]
                    total_size += bases[f]['server_size']

        else:
            bases = self.bases
            for f in bases:
                total_size += bases[f]['server_size']

        self.progressBar = PW.PW(
            Title = 'Скачиваем свежую номерную ёмкость',
            MaxCount = total_size,
            H1 = 'Скачиваем последнюю версию номерной ёмкости.',
            Descr = 'Общий объём $$ Кб.'
        )

        self.UpdateThread = UpdateThread(MW=self, bases=bases)
        self.UpdateThread.start()

        # self.closeWindow()
        # self.setVisible(False)

    def Update_neutral(self):
        self.clear_layout(self.Hlayout)


    # def clear_layout(self, layout):
    #     for i in range(layout.count()):
    #         child = layout.itemAt(i).widget()
    #         child.deleteLater()


    def closeProgram(self):
        self.MainWindow.close()
        self.close()


    def closeWindow(self):
        self.close()


class UpdateThread(QThread):
    progressChanged = Signal(int)
    def __init__(self, MW, bases:dict):
        super(UpdateThread, self).__init__()
        self.MW = MW
        self.bases = bases
        self.progressChanged.connect(self.MW.progressBar)


    def run(self):
        print('получили ' + str(len(self.bases)))
        print(self.bases)


        for f in self.bases:
            f


        self.progressChanged.emit(12500)

