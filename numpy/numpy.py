#Problem 1
import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

print('Distict Overlapping values ' + str(np.intersect1d(a,b)))

#Problem 2
arr = np.arange(1,16).reshape(5,3,order='F')
print('5x3 array with numpy functionality : ')
print(arr)

#Problem 3
print( "Following 2D array to the 1D array/ flattened form : "+ str(arr.flatten('F')) )

#Problem 4
threeDArr = arr.reshape(3,5,1)
print( "Following 5x3 2D Array from Problem 2 into 3D form : ")
print(threeDArr)

#Problem 5
twoDArr = threeDArr.reshape(5,3)
print('3D array from problem 4 back into 2D form using numpy: ')
print(twoDArr)

#Problem 6
a = np.array([12, 5, 7, 15, 3, 1, 8])
b = np.array([14, 6, 3, 11, 19, 12, 5])

newArr = np.setdiff1d(a,b)
print('a-b using python : ')
print(newArr)

#Problem 7
#reading Module6_data from uploaded github file
df = pd.read_csv("https://raw.githubusercontent.com/hassanamjad1/CS381HW/main/numpy/Module6_Data.csv")

##1
print('Maximum Yearly NYC consumption of water (millions of gallons per day) :')
df['NYC Consumption(Million gallons per day)'].max()

##2
print('Calendar years in the data' + str(np.shape(df)[0]))

##3
per_capita_consumption = df['Per Capita(Gallons per person per day)']
print('Mean of per capita : ')
print(np.mean(per_capita_consumption))

print('Standard Deviation of per capita : ')
print(np.std(per_capita_consumption))

##4
print('Differences b/w population from year 1979 to 2017 : ')
population = df['New York City Population']
pop_diff = np.diff(population);
print(pop_diff)






