from params import P, Params
import Update as upd
import Excel
import fff as f
from Dialog_Update import Update_Ask
import urllib.request
from MakeClassFromUI import ClassFromUI
from datetime import datetime, date
import time
import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QCoreApplication, Qt, Slot

#! Если плохо распозналась кодировка файла то дать возможность ввести кодировку в ручную
#! Надо проверить есть ли файлы вообще
#! Адрес от куда берутся обновления чтобы можно было редактировать в настройках
#! Проверка и обновление основного ПО
#! Поискать список перебежчиков.

prm = Params()

ClassUI = ClassFromUI(P + 'UI.ui')
class UI(QMainWindow, ClassUI):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)

        self.SrcFullPathFile = ''
        self.BTN_Browse.clicked.connect(self.BTN_Open)
        self.TBTN_Reset_Path.clicked.connect(self.BTN_Open_Reset)

        is_db = upd.Check_Arrays()
        self.show()

        #! После успешного обновления отметить в базе дату когда прошли обновления
        # Если все файлы номерной ёмкости найдены
        if is_db == 'all_good':
            different_date = abs((date.today() - prm.last_Update).days)
            if different_date >= prm.update_frequency:
                old_bases = upd.Check_Update_Arrays()
                if type(old_bases) == dict:
                    self.Update_Ask = Update_Ask(self, bases=old_bases)
            
        # Если папка с файлами номерной ёмкости вообще не найдена
        elif is_db == 'no_folder':
            self.BTN_Browse.setEnabled(False)
            self.Update_Ask = Update_Ask(self, bases=is_db)
        
        # Если хоть один из файлов номерной ёмкости не найден
        else:
            self.BTN_Browse.setEnabled(False)
            need_bases = upd.Check_Update_Arrays_for_present(is_db)
            self.Update_Ask = Update_Ask(self, bases=need_bases)

        # self.BTN_Render.setEnabled(True)



    @Slot(int)
    def ProgressWindow(self, i):
        print(i)

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

                    tmp = self.SrcContent.Get_First_20_Rows()
                    self.Col_w_Phone = f.find_Col_w_Phone(tmp, self.header)
                    if self.Col_w_Phone:
                        self.SPINBOX_Column_w_Phone.setValue(self.Col_w_Phone + 1)
                    else:
                        self.SPINBOX_Column_w_Phone.setValue(0)

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
        print('Резет')

    def Read_SrcContent(self):
        Src_FileName = os.path.basename(self.SrcFullPathFile)
        self.Src_FileName, self.Src_FileExtension = os.path.splitext(Src_FileName)
        
        SrcContent = Excel.Read(self.SrcFullPathFile)
        if self.Src_FileExtension.lower() == '.csv':        
            encode = f.get_encode_file_auto(self.SrcFullPathFile)
            print('Кодировка файла определена как "' + encode + '"')
            self.sep = f.find_separator(self.SrcFullPathFile, encode)
            print('Разделитель определен как "' + self.sep + '"')
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
