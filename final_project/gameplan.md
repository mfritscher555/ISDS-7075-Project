# Gameplan

## Goal: 

Minimize Root Mean Square Error of predictions of energy consumptio (load) given temperature data

## One idea:

Predict total load per day using temperature as a predictor while using relative percentages to determine the load produced 
by each station. If we can say that each station has a consistent relative load, then we can use these percentages to find
the load by station from the total.


## Another idea
Use some sort of clustering model to associate which of the 9 weather stations correlate with each of the 15 powerplants.
Then use these weights as predictive variables.

Association Rules??

## Note from Dr. Chun

There are 15 towns and cities in the state of Louisiana and 9 weather stations across the state.  The exact names and locations are unknown.  Your goal is to predict the demand for electricity for each town.  Some weather stations are close to the town, whereas others are far away.  Thus, you need to develop multiple regression model, for example.  For example, the electricity demand in Baton Rouge is more related to the temperature in Hammond than the temperature in Shreveport.


