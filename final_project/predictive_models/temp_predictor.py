import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from neuralprophet import NeuralProphet
from sklearn.linear_model import LinearRegression

# Relative path wont work. sorry guys...
total_loads = pd.read_csv(r"C:\Users\Matthew\PycharmProjects\ISDS-7075-Project\final_project\datasets\total_load.csv")
total_loads.reindex(
    ['day', 'month', 'year', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13', 'h14',
     'h15', 'h16', 'h17', 'h18', 'h19', 'h20', 'h21', 'h22', 'h23', 'h24', 'h1', ])

temps = pd.read_excel(r"C:\Users\Matthew\PycharmProjects\ISDS-7075-Project\final_project\datasets\dataset.xlsx",
                      sheet_name="temperature_history")

# Creating dummy variables for each of the 9 weather stations
temps = pd.get_dummies(temps, columns=["station_id"])
# temps.info()

# Will predict h1 temp for station 1
# Create a new dataframe that only contains station 1 data

station1 = temps.loc[temps['station_id_1'] == 1]

# station1.to_excel("station1_temps.xlsx")

# Creating a datetime column (required in order for the NeuralProphet() function to work
station1["date"] = pd.to_datetime(station1[["year", "month", "day"]], format='%Y-%m-%d', errors='coerce')

print(station1["date"].head())

# This creates a time-series graph of temperature from h1 for observations 0-14715 (until the df is empty)
# plt.plot(station1.loc[0:14706,'date'], station1.loc[0:14706, 'h1'])
# plt.show()


new_df = station1[['date', 'h1']]
new_df.dropna(inplace=True)
new_df.columns = ['ds', 'y']
print(new_df.tail())

# Training the model

n = NeuralProphet()
model = n.fit(new_df)

# Forecasting

future = n.make_future_dataframe(new_df, periods=7, n_historic_predictions=len(new_df))
forecast = n.predict(future)
n.plot(forecast).savefig('h1_s1_forecast.png')
plt.show()

# RMSE is ~ 6.54
# Need to set random seed in order to reproduce identical results


# forecast.info()
# print(forecast[["ds","yhat1"]].tail(7))

# Saving predictions to a df, but can later append this to the original dataframe and use that df to predict energy
# demand

predictions = forecast[["ds", "yhat1"]].tail(7)
predictions.to_excel("h1_predictions.xlsx")
