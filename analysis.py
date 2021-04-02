# Code for pands-project2021
# Author: Daniel Gonzalez



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


### --- Description:

dataset = pd.read_csv("iris.data.csv", header=None, names=["sepal length", "sepal width", "petal lenght", "petal width", "variety"])
# Reads data from file

print(dataset.head(1))
#prints 1 instance as a sample

variable_summary = dataset.groupby("variety").describe()
# Describes all variables grouped by variety of flower

variable_summary.to_csv("summary.txt")
#saves the summary as a text file

variable_summary.to_csv("summary_table.txt")
# Copy of the file as a readable table


# Accessing data grouped by each variety
setosa = dataset[dataset["variety"] =="Iris-setosa"]
versicolor = dataset[dataset["variety"] =="Iris-versicolor"]
virginica = dataset[dataset["variety"] =="Iris-virginica"]


#Printing description of each variety
print("Iris setosa:")
print(setosa.describe())

print("Iris versicolor:")
print(versicolor.describe())

print("Iris virginica:")
print(virginica.describe())


### --- Visualisation:

dataset.hist(color = "darkslateblue", edgecolor="yellow")
# Changing colors of histogram

plt.savefig(fname="histograms.png")
# Saves the histograms to a .png file

sns.pairplot(dataset, hue="variety")
#plt.savefig(fname="scatterplot.png")

plt.show()
# Display plot

