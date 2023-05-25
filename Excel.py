import pandas as pd

class Read:
    def __init__(self, inputFile):
        self.inputFile = inputFile
        
    def Read_xlx(self):
        self.DF = pd.read_excel(self.inputFile)

    def Read_csv(self, sep):
        self.DF = pd.read_csv(self.inputFile, sep=sep, encoding_errors='ignore')

    def GetFullDataFrame(self):
        return self.DF
    
    def GetListAllCols(self):
        return self.DF.columns.tolist()

    def CountDuplicateColumn(self, ColumnName):
        tmp = self.DF.filter(like=ColumnName).count()
        return len(tmp) - 1 

    def GetFullData(self):
        return self.DF.values

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