# проверить размер файла на сервере
import urllib.request
from params import P, Params
import Update as upd
from MakeClassFromUI import ClassFromUI
import Excel
from datetime import datetime, date
import time
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
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
        

        self.BTN_Browse.clicked.connect(self.BTN_Open)
        self.TBTN_Reset_Path.clicked.connect(self.BTN_Open_Reset)


        self.show()

    def BTN_Open(self):
        print('Опен')
        path = QFileDialog.getOpenFileName(
            parent=None,
            caption='Выбрать XLSX, XLS или CSV файл',
            dir=os.environ['USERPROFILE'] + '\Desktop',
            filter='Excel File (*.xlsx *.xls *.csv)',
            initialFilter='Excel File (*.xlsx *.xls *.csv)'
        )[0]
        if not path == '':
            self.SrcFullPathFile = path.replace('/', '\\')
            Src_FileName = os.path.basename(self.SrcFullPathFile)
            self.Src_FileName, self.Src_FileExtension = os.path.splitext(Src_FileName)
            self.LE_Path.setText(self.FullPathFile)

            if not self.SrcFullPathFile == '':
                self.SrcContent = Excel.Read(self.SrcFullPathFile)

                Src_ListAllCols = self.SrcContent.GetListAllCols()
                print(Src_ListAllCols)
                # self.Columns_SrcNew.clear()
                # self.SrcNew_SelectedColumns.clear()
                # if len(self.AsGoodPrecision) > 0:
                #     self.btnGenerateOutput.setEnabled(True)
                # tmp = []
                # for col in Src_ListAllCols:
                #     self.Columns_SrcNew.addItem(col)
                #     if col in prm.SrcNew_cols_with_address:
                #         tmp.append(col)


            else:
                del self.SrcNew
                self.BTN_Open_Reset()



    def BTN_Open_Reset(self):
        print('НЕ Опен')


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    Window = UI()
    sys.exit(app.exec())
