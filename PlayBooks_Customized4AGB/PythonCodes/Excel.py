from pandas import ExcelWriter
import glob
import os
import pandas as pd

writer = ExcelWriter("MMIX_OCT.xlsx")
os.chdir(r"C:\Users\ayeny\OneDrive\Desktop\MMIX OCT")
for filename in glob.glob("*.xlsx"):
    excel_file = pd.ExcelFile(filename)
    (_, f_name) = os.path.split(filename)
    (f_short_name, _) = os.path.splitext(f_name)
    for sheet_name in excel_file.sheet_names:
        df_excel = pd.read_excel(filename, sheet_name=sheet_name)
        df_excel.to_excel(writer, f_short_name+'_'+sheet_name, index=False)

writer.save()
