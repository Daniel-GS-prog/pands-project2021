# Code for pands-project2021
# Author: Daniel Gonzalez


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv("iris.data.csv")
# Reads data from file

dataset.columns = ["sepal length", "sepal width", "petal lenght", "petal width", "variety"]
# Definning attributes

#print(dataset.head(1))
#prints 1 instance as a sample

variable_summary = dataset.describe() 
#print(variable_summary)

variable_summary_t = variable_summary.transpose() 
# Prints a summary of each variable

#print(dataset.groupby("variety").size())

#variable_summary_t.to_csv("summary.txt")


