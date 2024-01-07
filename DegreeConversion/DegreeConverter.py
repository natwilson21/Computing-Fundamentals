# Assignment 2, Question 1
# Created by Natalia Wilson

'''
# Implement a Fahrenheit function that returns the Fahrenheit equivalent of a Celsius temperature.
# Print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the range
 -10 to 100 degrees. Use three digit percision for the results. Print the outputs in a neat
  tabular format. 
'''

def tempChart(curList):
    print("Celsius  Fahrenheit")
    for i in range(-10,101):
        equationF2C = (9/5)*i + 32
        print(f'{i}', end = '        ')
        print(f'{equationF2C:.3f}')
        
CtoFList = []
for k in range(-10,101):
    CtoFList.append(range(-10,101))
tempChart(CtoFList)