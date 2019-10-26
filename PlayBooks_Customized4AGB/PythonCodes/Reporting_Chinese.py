import glob
import os
import pandas as pd
writer = ExcelWriter("China Cloud Customers & Testing xx_xx_xxxx")
os.chdir(r"X:\CLOUD\AGB China\China Cloud VM lists")
filename = input("Type the file name to send out: ")
excel_file = pd.ExcelFile(filename)
