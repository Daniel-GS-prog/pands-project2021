# Code for pands-project2021
# Author: Daniel Gonzalez


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv("iris.data.csv", header=None, names=["sepal length", "sepal width", "petal lenght", "petal width", "variety"])
# Reads data from file


print(dataset.head(1))
#prints 1 instance as a sample

variable_summary = dataset.groupby("variety").describe()
# Describes all variables grouped by variety of flower

#variable_summary.to_csv("summary.txt")
#saves the summary as a text file

#variable_summary.to_csv("summary_table.txt")
# Copy of the file as a readable table

setosa = dataset.loc[:49]
versicolor = dataset.loc[49:99]
virginica = dataset.loc[99:]
# Setting indexes for each variety

""" s = setosa.describe()
ver = versicolor.describe()
vir = virginica.describe() """
# Defines a descrive function to each variety

#print(s)
#print(ver)
#print(vir)
# Prints each description


dataset.hist(color = "darkslateblue", edgecolor="yellow")
# Changing colors of histogram

#plt.savefig(fname="variable_histograms.png")
# Saves the histograms to a .png file

#plt.show()
# Display plot

