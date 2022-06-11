import csv
import pandas as pd

#1
headers = ["Price","Maintenance Cost","Number of doors","Number of passengers","Luggage capacity","Safety Rating","Classification of vehicle"]
df = pd.read_csv("https://raw.githubusercontent.com/hassanamjad1/CS381HW/main/uploading_and_processing_data/cars-sample35.csv",header=None)
# headers = ["Price","Maintenance Cost","Number of doors","Number of passengers","Luggage capacity","Safety Rating","Classification of vehicle"]
df.to_csv("new.csv",header=headers,index=False)
newDf = pd.read_csv("new.csv")

#2
# creating seven distinct python lists for each value 
prices = newDf['Price'].to_list()
maintenance_costs = newDf['Maintenance Cost'].to_list()
no_of_doors = newDf['Number of doors'].to_list()
no_of_passengers = newDf['Number of passengers'].to_list()
luggage_cappacity = newDf['Luggage capacity'].to_list()
saafety_rating = newDf['Safety Rating'].to_list()
classification_vehicle = newDf['Classification of vehicle'].to_list()

#3
carslist_with_medium_prices = []
for i in range(len(prices)):
  if prices[i] == "med":
    carslist_with_medium_prices.append(i)
print("Cars index for medium prices : " + str(carslist_with_medium_prices))

#4
no_passengers_medium_prices = []
for i in range(len(prices)):
  if prices[i] == "med":
    no_passengers_medium_prices.append(no_of_passengers[i])
print("No of Passengers for medium prices cars : " + str(no_passengers_medium_prices))

#5
carslist_with_highPrice_notLow_maintenance = []
for i in range(len(prices)):
  if prices[i] == "high" and maintenance_costs[i] != "low":
     carslist_with_highPrice_notLow_maintenance.append(i)
print("Cars index for high prices cars and not low maintenance fees : " + str(carslist_with_highPrice_notLow_maintenance))

#6
carslist_with_medium_prices2 = [i for i in range(len(prices)) if prices[i] == 'med']
print("Cars index for medium prices using list comprehension : " + str(carslist_with_medium_prices2))

#7
no_passengers_medium_prices = []
for i in range(len(prices)):
  if prices[i] == "med":
    no_passengers_medium_prices.append(no_of_passengers[i])
print("No of Passengers for medium prices cars : " + str(no_passengers_medium_prices))

#8
carslist_with_highPrice_notLow_maintenance = []
for i in range(len(prices)):
  if prices[i] == "high" and maintenance_costs[i] != "low":
     carslist_with_highPrice_notLow_maintenance.append(i)
print("Cars index for high prices cars and not low maintenance fees : " + str(carslist_with_highPrice_notLow_maintenance))

#Nested List Comprehension (no file needed):
#1
nlist = [ [1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E'] ]
individual_element = [element for List in nlist for element in List ]
print(individual_element)
# without using nested for loop inside list comprehension (from udemy course)
print(sum(nlist,[]))

#link to colab.research.google.com : https://colab.research.google.com/drive/1faEilrioX9Cx5-dCJOqJSBylAd9a3FmO?usp=sharing









