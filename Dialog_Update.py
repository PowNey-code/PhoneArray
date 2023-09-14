from PySide6.QtWidgets import QDialog, QStyle, QVBoxLayout, QLabel, QDialogButtonBox, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Update_Ask(QDialog):
    # def __init__(self, MainWindow):
    def __init__(self, bases):
        super(Update_Ask, self).__init__()
        
        self.setModal(True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_BrowserReload))
        self.setWindowFlags(Qt.WindowSystemMenuHint)
        self.setWindowTitle('Обновление номерных ёмкостей')
        self.resize(250, 200)

        # self.MainWindow = MainWindow
        self.bases = bases
        print(type(bases))
        print(bases)

        if type(bases) == dict:
            # Если некоторые файлы отсутствуют и возможно некоторые нужно обновить
            if any([bases[f]['status'] == 'no_file' for f in bases]):
                print('нашли')

            # Если все файлы найдены но нуждаются в обновлении
            else:
                print('не нашли')
                for i, file in enumerate(bases, start = 0):
                    if i == 0:
                        newest_date = bases[file]['server_date']
                        oldest_date = bases[file]['local_date']

                    if oldest_date > bases[file]['local_date']:
                        oldest_date = bases[file]['local_date']

                    if newest_date < bases[file]['server_date']:
                        newest_date = bases[file]['server_date']

                mess = f"Доступны новые версии номерных ёмкостей (<span style='color:green'>{newest_date.strftime('%d.%m.%Y')}</span>), сейчас установленны <span style='color:red'>{oldest_date.strftime('%d.%m.%Y')}</span>.<br>Скачать обновления?"
                

        else:
            pass
            # Нужно сообщить что папка с номерной ёмкостью не обнаружена, и предложить скачать их

        self.Answer = QLabel(mess)
        self.Answer.setFont(QFont('Verdana', 10))

        self.btn_update_all = QPushButton("Обновить", default=True)
        self.btn_update_all.setFont(QFont('Verdana', 11))
        self.btn_update_all.setStyleSheet("color: green;")
        self.btn_update_all.setFixedSize(180, 42)

        self.btn_cancel = QPushButton("Напомнить следующий раз", autoDefault=False)
        self.btn_cancel.setFont(QFont('Verdana', 11))
        self.btn_cancel.setStyleSheet("color: red;")
        self.btn_cancel.setFixedSize(250, 42)

        self.btn_box = QDialogButtonBox()
        self.btn_box.addButton(self.btn_update_all, QDialogButtonBox.AcceptRole)
        self.btn_box.addButton(self.btn_cancel, QDialogButtonBox.RejectRole)

        self.Vlayout = QVBoxLayout(self)
        self.Vlayout.addWidget(self.Answer)
        self.Vlayout.addWidget(self.btn_box)
    
        # btn_update_all.clicked.connect(lambda: MainWindow.dialog_report(question='y', SenderName='direction'))
        # btn_cancel.clicked.connect(lambda: MainWindow.dialog_report(question='n', SenderName='direction'))
        self.show()

    def Update(self):
        pass