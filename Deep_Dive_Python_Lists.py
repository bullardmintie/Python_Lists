#Task 1 -- Find out which students both submitted their
#assignments and attended the class

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

same_numbers = set(submitted).intersection(set(attended))
print(same_numbers)


#Task 2 -- Check if the two lists are identical in terms
#of their content, regardless of order

if submitted == attended:
    print("Both lists are identical!")
else:
    print("Both lists are not identical!")


#Task 3 -- Using list methods, remove any student from the
#attended list who did not submit their assignment (Eve, Frank)

attended.remove("Eve")
attended.remove("Frank")
print(attended)