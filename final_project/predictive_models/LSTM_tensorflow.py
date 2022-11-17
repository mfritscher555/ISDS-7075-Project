
# The goal of this file is to predict temperature for all 9 stations for all 24 hours for 7 days

# We also want to include the n
# on-time dependent variables, i.e., include variables that indicate the station number (locations)
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Dropout
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns



# Reading in data
temps = pd.read_excel(r"C:\Users\Matthew\PycharmProjects\ISDS-7075-Project\final_project\datasets\dataset.xlsx",
                      sheet_name="temperature_history")

# Creating dummy variables for each of the 9 weather stations
temps = pd.get_dummies(temps, columns=["station_id"])

# Creating a date field
temps["date"] = pd.to_datetime(temps[["year", "month", "day"]], format='%Y-%m-%d', errors='coerce')
train_dates = temps["date"]

# Identifying which cols for training (h1 is the y in this example)
cols = list(temps)[4:-1]


# New df with only x vars
df_for_training = temps[cols].astype(float)
df_for_training = df_for_training.iloc[0:14715,:]





# # Splitting data into training and testing sets
# x, x_test, y, y_test = train_test_split(df_for_training, df_for_training['h1'], test_size=0.15, shuffle=True)
#
#
# # Split the remaining data to train and validation
# x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.15, shuffle=True)

# LTSM uses sigmoid and tanh that are sensitive to magnitude, so values need to be normalized
scaler = StandardScaler()
scaler = scaler.fit(df_for_training)
df_for_training_scaled = scaler.transform(df_for_training)



trainX = []
trainY = []




n_future = 1
n_past = 14



for i in range(n_past, len(df_for_training_scaled) - n_future + 1):
    trainX.append(df_for_training_scaled[i - n_past:i, 0:df_for_training.shape[1]])
    trainY.append(df_for_training_scaled[i + n_future - 1:i + n_future, 0])

trainX, trainY = np.array(trainX), np.array(trainY)

# print(trainX)
# print(trainY)



# define Autoencoder model

model = Sequential()
model.add(LSTM(64, activation='relu', input_shape=(trainX.shape[1], trainX.shape[2]), return_sequences=True))
model.add(LSTM(32, activation='relu', return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(trainY.shape[1]))

model.compile(optimizer='adam', loss='mse')
model.summary()


# fit model
history = model.fit(x=trainX, y=trainY, epochs=10, batch_size=16, validation_split=0.1, verbose=1)

plt.plot(history.history['loss'], label='Training loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.legend()
plt.show()

# forecast_period_dates = pd.date_range(list(train_dates)[-1], periods=n_future, freq='1d').tolist()
#
# forecast = model.predict(x_train[-n_future])
#
# print(forecast)