#Task 1--sort grades in descending order

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)


#Task 2--calculate the average grade
average = sum(grades)/len(grades)
print(average)


#Task 3--replace any grade < 80 w/value Failed

for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
print(grades)