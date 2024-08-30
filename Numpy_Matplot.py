# 9. Numpy
#    Use the `numpy` library to create an array of numbers from 0 to 10 and calculate their sum.
        # NumPy is a library for the Python programming language,
        # adding support for large, multi-dimensional arrays and matrices,
        # along with a large collection of high-level mathematical functions to operate on these arrays.


import numpy as np          # The numpy library is imported using the import statement.
                            # The 'as' keyword is used to create an alias for the library.
                            # We need to import the library before using it in the program.

arr = np.arange(11)         # The np.arange() function creates an array of numbers from 0 to 10.
print("Array:", arr)        # We use 'np - dot' as prefix to access the functions and classes in the numpy library.
print("Sum:", np.sum(arr))  # The np.sum() function calculates the sum of all the elements in the array.


# 10. Matplotlib
#     Create a line plot that represents the function y = x^2 for values of x ranging from -10 to 10.
            # Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
            # It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

import matplotlib.pyplot as plt    # The matplotlib library is imported using the import statement.
import numpy as np

x = np.linspace(-10, 10, 100)       # The np.linspace() function is used to create an array of numbers.
                                    # np.linspace(start, stop, num) will generate 'num' evenly spaced numbers from 'start' to 'stop'.
y = x**2                            # The array 'x' is squared to get the values of 'y'.

plt.plot(x, y, label="y = x^2")     # The plt.plot() function is used to create a line plot.
plt.xlabel("x")                     # The x-axis label is set using the plt.xlabel() function.
plt.ylabel("y")                     # The y-axis label is set using the plt.ylabel() function.
plt.title("Plot of y = x^2")        # The title of the plot is set using the plt.title() function.
plt.legend()                        # The legend is displayed using the plt.legend() function.
plt.show()                          # The plot is displayed using the plt.show() function.
