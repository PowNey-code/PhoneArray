import pandas as pd

class Read:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        self.DF = pd.read_excel(self.inputFile)

    def GetFullDataFrame(self):
        return self.DF
    
    def SetCols(self, cols_with_address):
        address_in = []
        for col in cols_with_address:
            address_in += self.DF[col].tolist()

        # Удаляем дубликаты из списка
        self.UniqAddress = list(set(address_in))
        self.CountUniqAddress = len(self.UniqAddress)
        return self.GetUniqAddress()

    def GetListAllCols(self):
        return self.DF.columns.tolist()

    def CountDuplicateColumn(self, ColumnName):
        tmp = self.DF.filter(like=ColumnName).count()
        return len(tmp) - 1 

    def GetFullData(self):
        return self.DF.values

    def GetUniqAddress(self):
        return self.UniqAddress

    def GetCountUniqAddress(self):
        return self.CountUniqAddress

    def GetCountAllAddress(self):
        return len(self.DF.values) * 2

    def SetUniqAddress(self, NewListUniqAddress):
        if type(NewListUniqAddress == list):
            self.UniqAddress = NewListUniqAddress
        else:
            self.UniqAddress = list(NewListUniqAddress)
        self.CountUniqAddress = len(self.UniqAddress)
        
    def __del__(self):
        pass

class Write:
    def __init__(self, columns):
        self.table = {}
        for col in columns:
            self.table[col] = []

    def Add_Row(self, CurrentRow):
        for key in CurrentRow:
            self.table[key].append(CurrentRow[key])
    
    def ShowTable(self): return self.table

    def SaveFile(self, FileName):
        df = pd.DataFrame(self.table)
        writer = pd.ExcelWriter(FileName + '.xlsx') 
        try:
            df.to_excel(writer, sheet_name='Address', index=False, na_rep='NaN')
            for column in df:
                column_width = max(df[column].astype(str).map(len).max(), len(column))
                col_idx = df.columns.get_loc(column)
                writer.sheets['Address'].set_column(col_idx, col_idx, column_width)
            writer.close()
        except Exception: return False
        else: return True