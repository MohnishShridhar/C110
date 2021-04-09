import plotly.figure_factory as ff 
import pandas as pd 
import random
import csv
import plotly.graph_objects as go 
import statistics

df= pd.read_csv("data.csv")
data=df["temp"].to_list()

#code to find the mean of 100 data points a 1000 times and plot it
#function to get the mean of given data samples
#pass the number of data points you want as "counter"
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return(mean)

#function to plot the mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

#to call the random function 1000 times
def setup():
    mean_list=[]
    for i in range(0, 1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("Mean of sampling distribution: ", mean)

setup()
    
#to find the population mean
population_mean= statistics.mean(data)
print("Population mean: ", population_mean)

#to find standard deviation of sample data
def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution: ", std_deviation)

standard_deviation()