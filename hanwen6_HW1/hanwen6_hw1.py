# -*- coding: utf-8 -*-
"""hanwen6_HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VyB-xrjX-DeMulrLwGG588SlcXP2EXuV
"""

#Problem 2 b
#zero score of heights
heights_data = [193, 198, 190, 228, 210, 198, 208, 203, 216, 175, 183, 195]
mean_height = sum(heights_data) / len(heights_data)
differences_height = [(value - mean_height)**2 for value in heights_data]
sum_of_differences_height = sum(differences_height)
standard_deviation_height = (sum_of_differences_height / (len(heights_data))) ** 0.5
zero_scores_height = [(value  - mean_height) / standard_deviation_height for value in heights_data] 
print(zero_scores_height)

#zero score of weights
weights_data = [96, 98, 86, 140, 116, 92, 117, 113, 136, 81, 79, 92]
mean_weight = sum(weights_data) / len(weights_data)
differences_weight = [(value - mean_weight)**2 for value in weights_data]
sum_of_differences_weight = sum(differences_weight)
standard_deviation_weight = (sum_of_differences_weight / (len(weights_data))) ** 0.5
zero_scores_weight = [(value  - mean_weight) / standard_deviation_weight for value in weights_data] 
print(zero_scores_weight)

#Sample variance of heights
mean_height_norm = sum(zero_scores_height) / len(zero_scores_height)
var_height = sum((i - mean_height_norm) ** 2 for i in zero_scores_height) / (len(zero_scores_height))
print(var_height)

#Sample variance of weights
mean_weight_norm = sum(zero_scores_weight) / len(zero_scores_weight)
var_weight = sum((i - mean_weight_norm) ** 2 for i in zero_scores_weight) / (len(zero_scores_weight))
print(var_weight)

#Sample standard deviation of heights
stdev_height = (var_height)**0.5
print(stdev_height)

#Sample standard deviation of weights
stdev_weight = (var_weight)**0.5
print(stdev_weight)

#Problem 2 c
#Min-max normalization for heights and weights
import numpy as np

def normalize(x):
    min = np.min(x)
    max = np.max(x)
    range = max - min

    return [round((a - min) / range, 4) for a in x]


height = [193, 198, 190, 228, 210, 198, 208, 203, 216, 175, 183, 195]
weight = [96, 98, 86, 140, 116, 92, 117, 113, 136, 81, 79, 92]
normalized_height = normalize(height)
normalized_weight = normalize(weight)
print(normalized_height, normalized_weight)

#Sample variance of heights
mean_height_norm = sum(normalized_height) / len(normalized_height)
var_height = sum((i - mean_height_norm) ** 2 for i in normalized_height) / (len(normalized_height)-1)
print(round(var_height, 4))

#Sample variance of weights
mean_weight_norm = sum(normalized_weight) / len(normalized_weight)
var_weight = sum((i - mean_weight_norm) ** 2 for i in normalized_weight) / (len(normalized_weight)-1)
print(round(var_weight, 4))

#Sample standard deviation of heights
stdev_height = (var_height)**0.5
print(round(stdev_height, 4))

#Sample standard deviation of weights
stdev_weight = (var_weight)**0.5
print(round(stdev_weight, 4))

#Problem 4 C
A = [290, 428, 361, 103, 17]
B = [212, 347, 236, 78, 28]
sum = []
for i in range(len(A)):
  sum.append(A[i] + B[i])
#print(sum)
Exp = []
for i in range(len(sum)):
  Exp.append((1199 * sum[i])/2100)
for i in range(len(sum)):
  Exp.append((901 * sum[i])/2100)
#print(Exp)
chi_square = 0
for i in range(len(A)):
  chi_square += (A[i]-Exp[i])**2/Exp[i]
for i in range(len(B)):
  chi_square += (B[i]-Exp[len(A) + i])**2/Exp[len(A) + i]
chi_square

#Problem 5 b
import pandas as pd

file = pd.read_csv("automobile.csv")

data = file[["curb-weight", "horsepower", "city-mpg", "highway-mpg", "price"]]

cent_data = data - np.mean(data, axis = 0)

cov_mat = np.cov(cent_data.T)
eigvalues, eigvectors = np.linalg.eig(cov_mat)
#print(eigvalues)
#print(eigvectors)
temp_sort = np.argsort(eigvalues)[::-1]
sorted_eigvalues = eigvalues[temp_sort]
sorted_eigvectors = eigvectors[:, temp_sort][:, 0:2]

print(sorted_eigvalues, sorted_eigvectors.T)