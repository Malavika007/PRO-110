import csv
from matplotlib import lines
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random


df = pd.read_csv('Data.csv')

data = df['average'].tolist()
mean = statistics.mean(data)

fig = ff.create_distplot([data],["average"], show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataset =[]
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ['average'], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,1], mode = 'lines', name="Mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print('Mean of sampling distribution:-', mean)

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()
