# Set up a virtualenv
# be sure to pip install pandas 
# and pip install openpyxl

import pandas as pd



sheet2 = pd.read_excel("./final_project/datasets/dataset.xlsx", sheet_name="temperature_history")


"""There are 9 different stations where temperature was collected; the excel files shows data from each of the 9 stations
for each hour of each day. """



# Loading data from just station 1 
station1 = sheet2.loc[sheet2['station_id'] == 1]




