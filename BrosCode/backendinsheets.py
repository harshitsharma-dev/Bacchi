#Access google sheet this way(if we want to do it through sheets else ok)
import pandas as pd
import os
from datetime import datetime
# sheetid = "1s78u9kz70tp2BT-DOdoG30EwVnvPbkq2_PdXzE0-QcI"
# sheet_name = "Sheet1"
# #make csv of google sheet
# gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(sheetid,sheet_name)
# df = pd.read_csv(gsheet_url)#can type csv file location as well
#githublinkrawtocsv
url = "https://raw.githubusercontent.com/harshitsharma-dev/intern/main/Data%20input%20-%20Sheet1.csv"
df = pd.read_csv(url)
print(df)



#change values of data in dataframe
for i in range(len(df["Numbering"])):
    df["Numbering"][i] = i + 9;
print(df)



#or add with indexes simple df["Column name"][index]


#can convert data frame to list by append with indexes
#if required for heavy calculation
#can convert list to dataframe use pd.DataFrame(list)
#list should look like [[row1(elements like number, values, English)], [row2],[row3]]



#to convert dataframe to csv file
file_name = "filechanged"
df.to_csv(file_name)
os.system("git add .")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
os.system("git commit -m 'changed again{dt_string}'")
os.system("git push origin master")


