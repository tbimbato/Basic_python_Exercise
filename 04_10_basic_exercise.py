# Exercise 1: Sum of Two Numbers
# This function asks the user for two integers and prints their sum.
def sum_two_numbers():
    a = int(input("Enter first number: "))  # Ask for the first number and convert to integer.
    b = int(input("Enter second number: "))  # Ask for the second number and convert to integer.
    print("The sum is:", a + b)  # Print the sum of the two numbers.

# Exercise 2: Area of a Circle
# This function calculates the area of a circle given its radius.
def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))  # Get the circle radius from the user and convert to float.
    pi = 3.14159  # Define the approximation of Pi.
    area = pi * radius ** 2  # Calculate the area using the formula: Area = Pi * radius^2.
    print("Area of the circle is:", area)  # Print the area of the circle.

# Exercise 3: Check Even or Odd
# This function determines whether a given number is even or odd.
def check_even_odd():
    num = int(input("Enter a number: "))  # Ask the user for a number and convert it to an integer.
    if num % 2 == 0:  # Check if the number is divisible by 2 with no remainder.
        print(num, "is Even")  # If true, it's even.
    else:
        print(num, "is Odd")  # If false, it's odd.

# Exercise 4: Simple Interest Calculator
# This function calculates simple interest given principal, rate, and time.
def simple_interest():
    P = float(input("Enter the principal amount: "))  # Input the principal amount and convert to float.
    R = float(input("Enter the annual interest rate (as a percentage): "))  # Input the interest rate and convert to float.
    T = float(input("Enter the time in years: "))  # Input the time period in years and convert to float.
    SI = (P * R * T) / 100  # Calculate the simple interest using the formula: SI = (P*R*T)/100.
    print("The Simple Interest is:", SI)  # Print the calculated simple interest.

# Exercise 5: Maximum of Three Numbers
# This function returns the maximum of three given numbers.
def max_of_three():
    a = int(input("Enter first number: "))  # Input the first number and convert to integer.
    b = int(input("Enter second number: "))  # Input the second number and convert to integer.
    c = int(input("Enter third number: "))  # Input the third number and convert to integer.
    print("The maximum number is:", max(a, b, c))  # Print the maximum of the three numbers using the max() function.

# Exercise 6: Count Vowels in a String
# This function counts and prints the number of vowels in a given string.
def count_vowels():
    string = input("Enter a string: ")  # Ask the user to input a string.
    vowels = "aeiouAEIOU"  # Define a string of vowels (both lowercase and uppercase).
    count = sum(1 for letter in string if letter in vowels)  # Count the number of vowels in the string.
    print("Number of vowels in the string:", count)  # Print the count of vowels.

# Exercise 7: Factorial of a Number
# This function computes the factorial of a given number using a loop.
def factorial():
    n = int(input("Enter a number: "))  # Input a number and convert to integer.
    result = 1  # Initialize the factorial result to 1.
    for i in range(2, n + 1):  # Loop from 2 to n (inclusive).
        result *= i  # Multiply result by each i (this calculates the factorial).
    print("The factorial of", n, "is:", result)  # Print the factorial of the number.

# Exercise 8: Fibonacci Sequence
# This function prints the first 'n' numbers of the Fibonacci sequence.
def fibonacci():
    n = int(input("Enter the number of Fibonacci terms to display: "))  # Number of terms to display.
    a, b = 0, 1  # Initialize the first two Fibonacci numbers.
    for _ in range(n):  # Loop n times.
        print(a, end=' ')  # Print the current Fibonacci number.
        a, b = b, a + b  # Update the values of a and b.
    print()  # Print a newline after the sequence.

# Exercise 9: Palindrome Checker
# This function checks if a given string is a palindrome.
def palindrome_checker():
    s = input("Enter a string: ")  # Ask for a string from the user.
    if s == s[::-1]:  # Check if the string is equal to its reverse.
        print(s, "is a palindrome.")  # If true, print that it's a palindrome.
    else:
        print(s, "is not a palindrome.")  # If false, print that it's not a palindrome.

# Exercise 10: Convert Celsius to Fahrenheit
# This function converts temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))  # Input the Celsius temperature and convert to float.
    fahrenheit = celsius * 9/5 + 32  # Convert it to Fahrenheit using the formula: F = C * 9/5 + 32.
    print("Temperature in Fahrenheit:", fahrenheit)  # Print the temperature in Fahrenheit.

# Main function to run the exercises
def main():
    sum_two_numbers()
    area_of_circle()
    check_even_odd()
    simple_interest()
    max_of_three()
    count_vowels()
    factorial()
    fibonacci()
    palindrome_checker()
    celsius_to_fahrenheit()

if __name__ == "__main__":
    main()

    #PS this file has been created as a collection of defined functions,
    # and the main() function is called at the end to run all the exercises.
    # You can run each exercise individually by calling the respective function.
    # For example, to run the first exercise, you can call sum_two_numbers() directly.
    # This structure makes it easier to test and run each exercise separately.

    # in the terminal, you can run the file by typing `python 10_basic_exercise.py` or `python3 10_basic_exercise.py` depending on your Python version.
    # The program will execute all the exercises one by one and ask for user input where necessary.
    # You can also test each function separately by calling them directly in the terminal.
    # For example, you can run the factorial function by typing `factorial()` in the terminal.