
# 5. Lists
#    Write a program that takes a list of numbers from the user, sorts the list, and prints the maximum and minimum number.
lst = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
# This line contains multiple functions and methods:
# input() function takes a string from the user.
# split() method splits the string into a list of strings. By default, it splits on spaces.
# map() function applies the int() function to each element of the list.
# list() function converts the map object to a list.

# Another way to do the same thing:
while True:
    c = input("Enter a number or 'done' to finish: ")   # by entering one number at a time
    if c == "done":                                     # we can enter 'done' to finish entering numbers.
        break                                           # The break statement is used to exit a loop.
    lst.append(int(c))                                  # The append() method adds an element to the end of the list.


lst.sort()                          # The sort() method sorts the list in ascending order.
                                    # sort() method can take two arguments: key and reverse.
                                    # key is a function that will be used to compare the elements.
                                            # for example, key=abs will sort the list based on the absolute values.
                                            # other value avaible for the key argument are: str.lower, str.upper, etc.
                                    # reverse is a boolean value that specifies whether to sort in descending order.
                                    # sort(key=func, reverse=True) will sort the list in descending order using the func function. (10, 9, 8, 7, 6, ...) 
                                    # sort(reverse=False) will sort the list in ascending order. (1, 2, 3, 4, 5, ...)
print("Sorted list:", lst)          # The sorted list is printed using the print() function. No need to cycle through the list.
print("Maximum:", max(lst))         # The max() function returns the maximum value in the list.
print("Minimum:", min(lst))         # And the min() function returns the minimum value in the list.

# # # # # # # # # # # # # # # # # # # # # # # # # 


# 6. Dictionaries
#    Write a program that creates a dictionary with student names as keys and their scores as values. Print the average score.

# First: Dictionary are a collection of key-value pairs.
# for example: students = {     
#                               "Alice": 85,
#                               "Bob": 78,
#                               "Charlie": 92,
#                               "Diana": 88
#                         }
# So we have the student names as keys and their scores as values.
# We can have more complex values like lists, tuples, or even other dictionaries.
# Also, we can have a key and more than one value, like a list of scores for each student.

# Second: We can access the values in a dictionary using the keys.
# for example: students["Alice"] will return 85.
# If the key is not present in the dictionary, it will raise a KeyError.
# To avoid this, we can use the get() method, which will return None if the key is not found.
# for example: students.get("Alice") will return 85. (and the program will run without errors even if Alice doesn't exist in the dictionary)

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}


average = sum(students.values()) / len(students)    # The sum() function returns the sum of all the values in the dictionary.
                                                    # The len() function returns the number of items in the dictionary.
                                                    # The average is calculated by dividing the sum by the number of items.
                                                    # The / operator performs floating-point division.
                                                    # average = the sum of all the values in the dictionary divided by the number of items in the dictionary.
print("The average score is:", average)             # The average score is printed using the print() function.

# # # # # # # # # # # # # # # # # # # # # # # # # 


# 7. Tuples
#    Write a program that takes a list of tuples containing city names and their population. Print the name of the city with the maximum population.

# Tuple is a collection of items that are ordered and unchangeable.
# for example: cities = [("Verona", 257000), ("Venice", 260000), ("Milan", 1360000)]
# The difference between a list and a tuple is that a list is mutable, while a tuple is immutable.
# Why do we need tuples? Because they are faster than lists and can be used as keys in dictionaries.
# Tuples are created using parentheses, while lists are created using square brackets.

# variable = [1, 2, 3] is a list
# variable = (1, 2, 3) is a tuple

# Here we are making a list of tuples
# Each tuple contains the name of the city and its population.
 
cities = [("Verona", 257000), ("Venice", 260000), ("Milan", 1360000)]

# [("Verona", 257000), ... ] is a list of tuples like ("NameString, PopulationInt")

# We can access the elements of a tuple using indexing.

max_city = max(cities, key=lambda x: x[1])

# The max() function returns the item with the highest value in the iterable.
# The key argument specifies a function that will be used to compare the items.
# In this case, we are comparing the tuples based on the second element (population).
# The lambda function x: x[1] returns the second element of the tuple.
# let's analyze the arguments of the max() function:
        # 'cities' is the main variable (the list of tuples)
        # key=lambda x: x[1] is a function that will be used to compare the elements.
        # x is the parameter of the lambda function.
        # x[1] is the second element of the tuple.
        # this is quite confusing, but it's a common way to sort a list of tuples based on a specific element.

# Let's make an extra example to understand better the lambda function:
# for example:

lstTmp = [("Mario", 5.23, 41, 12), ("Luigi", 2.21, 44, 15), ("Peach", 1.05, 36, 0)]
# This is a list of tuples with 4 elements each.
# Find the max of the FIRST element of each tuple:
max_lstTmp1 = max(lstTmp, key=lambda x: x[0])   # Basically this select the String with the highest value AKA: "Mario" because it's the first element of the tuple.
# Find the max of the SECOND element of each tuple:
max_lstTmp2 = max(lstTmp, key=lambda x: x[1])   # This select the Float with the highest value, AKA: 5.23 because it's the second element of the tuple.
# Find the max of the THIRD element of each tuple:
max_lstTmp = max(lstTmp, key=lambda x: x[2])    # This select the Integer with the highest value, AKA: 44 because it's the third element of the tuple.
# Find the max of the FOURTH element of each tuple:

print("City with the highest population:", max_city[0]) # The name of the city with the maximum population is printed using the print() function.
                                                        # The max_city variable contains the tuple with the highest population.
                                                        # max_city[0] returns the first element of the tuple, which is the city name.

# # # # # # # # # # # # # # # # # # # # # # # # # 


# 8. Sets
#    Write a program that takes two sets of numbers from the user and prints their union, intersection, and difference.

    # Sets are collections of unique elements that are unordered and unindexed.
    # for example: set1 = {1, 2, 3, 4, 5}
    # Sets can be etheroegeneous, meaning they can contain different types of elements.
    # or.. set2 = {"apple", "banana", "cherry", 1, 2, 3, 4.234}


    # Let's firs understand the map() function:
        # The map() function applies a function to all the items in an input list.
        # The map() function takes two arguments: the function to apply and the list of items.
        # The function can be a built-in function or a user-defined function.
        # The map() function returns a map object, which is an iterator.
        # To convert the map object to a list, we can use the list() function.
        # The map() function can take multiple lists as input.

        # For example:
            # map(function, list)
            # map(int, ["1", "2", "3"]) will return [1, 2, 3] Because every element of the list is converted to an integer (int).

set1 = set(map(int, input("Enter the first set of numbers separated by spaces: ").split())) # The input() function returns a string, so we need to convert it to an integer.
set2 = set(map(int, input("Enter the second set of numbers separated by spaces: ").split()))    # The split() method splits the string into a list of strings. By default, it splits on spaces.

print("Union:", set1 | set2)            #    |     is the union operator. It combines the elements of both sets.
print("Intersection:", set1 & set2)     #    &     is the intersection operator. It returns the common elements of both sets.
print("Difference:", set1 - set2)       #    -     is the difference operator. It returns the elements that are in set1 but not in set2.


# # # # # # # # # # # # # # # # # # # # # # # # # 
# Continue to the next file: 03_Numpy_Matplot.py