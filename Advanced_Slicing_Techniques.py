#Task 1 -- Extract the temperatures for the
#second week (7 days) of the month. Expected Outcome:
#83, 85, 86, 87, 88, 89, 90

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

next_week = temperatures[7:14]
print(next_week)


#Task 2 -- Extract all the temperatures above 100

above = [i for i in temperatures if i > 100]
print(above)


#Task 3 -- Reverse the list and extract temperatures
#from the 5th to the 10th day of the reversed list

temperatures.reverse()
del temperatures[4:10]
print(temperatures)