# проверить размер файла на сервере
import urllib.request
from params import P, Params
import Update as upd
from MakeClassFromUI import ClassFromUI
import Excel
import fff as f
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

        self.SrcFullPathFile = ''
        self.BTN_Browse.clicked.connect(self.BTN_Open)
        self.TBTN_Reset_Path.clicked.connect(self.BTN_Open_Reset)

        # self.BTN_Render.setEnabled(True)


        self.show()

    def BTN_Open(self):
        path = QFileDialog.getOpenFileName(
            caption='Выбрать XLSX, XLS или CSV файл',
            dir=os.environ['USERPROFILE'] + '\Desktop',
            filter='Excel File (*.xlsx *.xls *.csv)',
            selectedFilter='Excel File (*.xlsx *.xls *.csv)'
        )[0]
        if not path == '':
            self.SrcFullPathFile = path.replace('/', '\\')
            
            self.LE_Path.setText(self.SrcFullPathFile)

            if not self.SrcFullPathFile == '':
                self.SrcContent = self.Read_SrcContent()
                if self.SrcContent:
                    self.Src_ListAllCols = self.SrcContent.GetListAllCols()

                    self.header = f.find_header(self.Src_ListAllCols)
                    if self.header:
                        self.RADIO_Head_Y.setChecked(True)
                    else:
                        self.RADIO_Head_N.setChecked(True)

                    self.Src_LenAllCols = len(self.Src_ListAllCols)
                    self.SPINBOX_Column_w_Phone.setMaximum(self.Src_LenAllCols)
                    self.SPINBOX_Insert_After.setMaximum(self.Src_LenAllCols)

                    print(self.Src_ListAllCols)
                    print(self.Src_LenAllCols)
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
                    # параметры файла не определены
                    pass

            else:
                self.BTN_Open_Reset()



    def BTN_Open_Reset(self):
        self.BTN_Render.setEnabled(False)
        self.LE_Path.setText('')
        self.LE_Separator.setText('')
        self.SrcFullPathFile = ''
        print('НЕ Опен')

    def Read_SrcContent(self):
        Src_FileName = os.path.basename(self.SrcFullPathFile)
        self.Src_FileName, self.Src_FileExtension = os.path.splitext(Src_FileName)
        
        SrcContent = Excel.Read(self.SrcFullPathFile)
        if self.Src_FileExtension.lower() == '.csv':        
            encode = f.get_encode_file_auto(self.SrcFullPathFile)
            self.sep = f.find_separator(self.SrcFullPathFile, encode)
            if self.sep:
                self.LE_Separator.setText(self.sep)
                SrcContent.Read_csv(self.sep, encode)
            else:
                return False
        else:
            self.LE_Separator.setText('Не требуется')
            SrcContent.Read_xlx()

        return SrcContent

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    Window = UI()
    sys.exit(app.exec())
