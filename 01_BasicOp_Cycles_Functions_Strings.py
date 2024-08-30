
# 1. Basic Operations
#   Write a program that asks the user for two numbers and displays
#    - the sum
#    - difference
#    - product
#    - quotient (both regular and integer division)
#    - remainder of the division

# Solution
a = int(input("Enter the first number: "))  # input() returns a string, so we need to convert it to an integer
b = int(input("Enter the second number: ")) # input() can 'speak' to the user and show a message (Enter something..etc..).

print("Sum:", a + b)                # print() is a function that prints the value passed to it.
print("Difference:", a - b)         # The value can be a string, integer, float, etc.
print("Product:", a * b)            # It can also be a variable or an expression.
print("Division:", a / b)           # The print() function can take multiple arguments.
print("Integer Division:", a // b)  # It will print all the arguments separated by a space.
print("Remainder:", a % b)          # The default separator is a space, but it can be changed using the sep argument.

# # # # # # # # # # # # # # # # # # # # # # # # # 

# 2. Conditions and Loops
#  Write a program that checks if a number is even or odd, and prints the even numbers from 0 up to the number entered by the user.


# solution
n = int(input("Enter a number: "))  

if n % 2 == 0:                      # The % operator returns the remainder of the division.
    print(f"{n} is even")           # If the remainder is 0, the number is even.
else:                               # We have to use '{}' to insert the value of n in the string.
    print(f"{n} is odd")            # The 'f' before the string indicates that it is a formatted string.
                                    # We can also use the format() method to insert values in a string.
                                    # Or simply use ' print(n, "is even") ' without the 'f' or format() method.
for i in range(0, n+1, 2):          # The range() function generates a sequence of numbers. 
    print(i)                        # It takes three arguments: start, stop, and step.
                                    #  range(start, stop, step) (from start, to stop with 'step' dimensioned step)

# # # # # # # # # # # # # # # # # # # # # # # # # 

# 3. Functions
#   Write a function that takes two numbers and returns the maximum of the two.

def max_num(a, b):                  # Functions are defined using the 'def' keyword.
    return a if a > b else b        # The 'return' statement is used to return a value from a function.
                                    # After the 'run' of a function is completed, the control is returned to the caller.

x = int(input("Enter the first number: "))      # input(), print() and other are built-in functions in Python.
y = int(input("Enter the second number: "))

print("The maximum number is:", max_num(x, y))  # We can call a function by using its name followed by parentheses.
                                                # We can pass arguments to the function inside the parentheses.
                                                # Function as a parameter to another function is also possible!

# # # # # # # # # # # # # # # # # # # # # # # # # 

# 4. Strings
#    Write a program that takes a string from the user and prints the reversed string and the number of characters in it.

s = input("Enter a string: ")       # The input() function returns a string, so python will treat it as a string.
                                    # the 's' variable will store the string entered by the user.

print("Reversed string:", s[::-1])  # We can reverse a string by using the slicing operator.
                                    # or by using the reversed() function.
                                    # s[::-1] slicing operator [start:stop:step] (start, stop, step)
                                    # if we don't specify the start and stop, it will take the whole string.
                                    # if we don't specify the step, it will take the default step of 1.         
                                    # if the step is negative, it will start from the end of the string.

print("Number of characters:", len(s))      # The len() function returns the length of the string.


# # # # # # # # # # # # # # # # # # # # # # # # # 
# Continue to the next file: 02_Lists_Dictsionaries_Tuples_Sets.py