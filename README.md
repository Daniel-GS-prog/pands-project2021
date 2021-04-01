# Fisher's Iris Dataset - Analysis

## Table of contents
* [Project Description](#Project-Description)
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Data set Description](#Dataset-Description)
* [Variables - Description](#Variables-Description)
* [Model's predictibility](#Model's-predictibility)
* [Conclusions](#Conclusions)
* [References](#References)

---

## Project Description
This research aims to analize the Ficher's Iris Dataset. First we will perform a description of all variables, after which we will test the predictability of the data.

Each segment will have a description and code samples.

The analysis is the final project of a module in Pytohn Programming, and the final goal is to refine our skills with python as a data analysis tool.

## Introduction
The Iris flower data set (or Ficher's Iris data set) is a multivariable data set created by the British statistician, eigenecist, and biologist Ronald Fisher in 1936. 

Ficher was not alone in this task. Dr. Edgar Anderson, a botanist from New York, is cited as the source of the data, which was collected at the Gaspé Peninsula, in Canada.

The data set has the attributes of 150 itis flowers. The goal was to create a linear function to differentiate iris species based on the morphology of their flowers.

The publication of "The Use of Multiple Measurements in TAxonomic Problems", had tremendous success, which is the reason why it's so widely used and studied. 

However, it's interesting to mention the context in which this research was conducted. Ficher was a vocal proponent of eugenics. "One of the points of the paper (and the journal, and of Fisher's leading roe in developing biometry and biostatistics) was to propose a methodological framework to delineate desirable traits, in support of eugenics programs."("Armchair Ecology, 2020")

Iris flowers varieties:

![alt Iris flower variety](iris_variety.jpeg)


---

## Technologies
For this project we used Python 3.7.6, and the following libraries:
``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

* Pandas will be used to summary the data.

* Matplotlib will create the histograms for each variable and variable combination

* With Seaborn we will display the scatterplots
---
## Data set Description
<br>

The source of the data set is :

```
http://archive.ics.uci.edu/ml/datasets/Iris
```
<br>
The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. 

The attributes are:
* Sepal length in cm
* Sepal width in cm
* Setal length in cm
* Setal width in cm
* class:
    * Iris Setosa
    * Iris Versicolour
    * Iris Virginica

<br>
FIrst, we will read the data with:

```python
dataset = pd.read_csv("iris.data.csv")

```

We can cjeck the number of instances for each variety with:
```python
dataset.groupby("variety").size()
```
Resulting in:
```python
variety
Iris-setosa        49
Iris-versicolor    50
Iris-virginica     50
dtype: int64
```

 With the following code we can structure the attribute's names and access a sample (first instance) of the database:

```python
dataset.columns = ["sepal length", "sepal width", "petal lenght", "petal width", "variety"]

dataset.head(1)
```

The result: 
 ```python
   sepal length  sepal width  petal lenght  petal width      variety
          4.9          3.0           1.4          0.2       Iris-setosa
```
 

---
## Variables - Description

We can access a summary of each variable with the following code:
```python
variable_summary = dataset.describe()
#The transpose() will make it easier to read:
variable_summary_t = variable_summary.transpose() 
print(variable_summary_t)

```

With the following result: 
```
|------------------------------------------------------------------|
|               count      mean       std  min  25%  50%  75%  max |
|------------------------------------------------------------------|
| sepal length  149.0  5.848322  0.828594  4.3  5.1  5.8  6.4  7.9 |
|------------------------------------------------------------------|
| sepal width   149.0  3.051007  0.433499  2.0  2.8  3.0  3.3  4.4 |
|------------------------------------------------------------------|
| petal lenght  149.0  3.774497  1.759651  1.0  1.6  4.4  5.1  6.9 |
|------------------------------------------------------------------|
| petal width   149.0  1.205369  0.761292  0.1  0.3  1.3  1.8  2.5 |
|------------------------------------------------------------------|
```


---
## Model's predictibility
---
## Conclusions
---
## References