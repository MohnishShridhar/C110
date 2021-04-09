import plotly.figure_factory as ff 
import pandas as pd 
import random
import csv
import plotly.graph_objects as go 
import statistics

df= pd.read_csv("data.csv")
data=df["temp"].to_list()

fig=ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()

mean=statistics.mean(data)
std_deviation=statistics.stdev(data)

print("Mean: ", mean)
print("Standard deviation: ", std_deviation)