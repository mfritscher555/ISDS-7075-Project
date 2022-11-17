import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from neuralprophet import NeuralProphet
from sklearn.linear_model import LinearRegression


# Goal: Write a function that outputs predictions for the 24 temperature predictions (and eventually for all station_ids)


total_loads = pd.read_csv(r"C:\Users\Matthew\PycharmProjects\ISDS-7075-Project\final_project\datasets\total_load.csv")
total_loads.reindex(
    ['day', 'month', 'year', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13', 'h14',
     'h15', 'h16', 'h17', 'h18', 'h19', 'h20', 'h21', 'h22', 'h23', 'h24', 'h1', ])

temps = pd.read_excel(r"C:\Users\Matthew\PycharmProjects\ISDS-7075-Project\final_project\datasets\dataset.xlsx",
                      sheet_name="temperature_history")

# Creating dummy variables for each of the 9 weather stations
temps = pd.get_dummies(temps, columns=["station_id"])


# here are the 9 station inputs:
station1 = temps.loc[temps['station_id_2'] == 1]
station2 = temps.loc[temps['station_id_2'] == 2]
station3 = temps.loc[temps['station_id_3'] == 3]
station4 = temps.loc[temps['station_id_4'] == 4]
station5 = temps.loc[temps['station_id_5'] == 5]
station6 = temps.loc[temps['station_id_6'] == 6]
station7 = temps.loc[temps['station_id_7'] == 7]
station8 = temps.loc[temps['station_id_8'] == 8]
station9 = temps.loc[temps['station_id_9'] == 9]


# This function creates the 24 dfs we will need
def temp_by_hour(station, h_number):
    # Creating date column for each station df
    station["date"] = pd.to_datetime(station[["year", "month", "day"]], format='%Y-%m-%d', errors='coerce')
    # h_number is a string, e.g., 'h1'
    new_df = station[["date", h_number]]
    return new_df

a = temp_by_hour(station1, 'h1')
print(a)


# A function similar to this one will pass in all 24 h vars into the function where xcols is a list
def ols_res(df, xcols,  ycol):
    return pd.DataFrame({xcol : sm.OLS(df[ycol], df[xcol]).fit().predict() for xcol in xcols})
    pass