# This exercise I will be playing with Numpy, although the idea is not to memorize methods, since we can always check the documentation - and stackoverflow :) - but to get familiarized with it.

import numpy as np


#Creating an array with numpy
a = np.array([1, 2, 3])
b = np.array([[9.0, 1.2, 3], [5.0, 3.0, 4.5]])
c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 12]]], dtype='int8')
print("A:", a)
print()
print("B:", b)
print()
print("C:", c)
print()
print()
# To get the dimensions of an array.
print("To get the number of dimensions use the .ndim result:")
print("A:", a.ndim)
print("B:", b.ndim)
print("C:", c.ndim)
print()
# To get the number of elements of each dimension.
print("To get the number of elements of each dimension use the .shape result:")
print("A:", a.shape) # It is only one dimension with 3 elements
print("B:", b.shape) # It is two dimensions, two sets, with 3 elements each
print("C:", c.shape)
print()
# To get the type of the data stored
print("To get the type of data stored use the .dtype result:")
print("A:", a.dtype) # Intergers
print("B:", b.dtype) # Floats
print("C:", c.dtype) # We defined we want int8 because we know the values are small
print()
# To get the size of each item
print("To get the size of each item use the .itemsize result:")
print("A:", a.itemsize) # 8 bits
print("B:", b.itemsize) # 8 bits
print("C:", c.itemsize) # 1 bit - because we defined the data type as int8, change 8 to 16, 32 or 64 and this number will increase
print()
# To get the size of the array
print("To get the size of the array use the .itemsize result:")
print("A:", a.nbytes)
print("B:", b.nbytes)
print("C:", c.nbytes)
print()

# Let's play with the arrays
# To get a specific element * Remember that the first position = 0
# 1 dimension array [position]: Let's say we want to retrieve the first element
print("The first element of A is:", a[0])
print()
# 2 dimension arrays [row, column]: Let's say we want to retrieve the first element in the second column
print("The second element of the second column of B is:", b[1,1])
print()
# 3 dimension arrays [dm, row, column]: Let's say we want to retrieve the second element of the first column
print("The second element of the first row of C is:", c[0, 0, 1])
print()
# But what if we want to retrieve an entire row or column?
print("The second column of B is:", b[1,:])
print()
print("The third row of B is:", b[:,2])
print()
# If we want to change an element:
print("Let's change the first element of each columns in B to 15")
b[:, 0] = 15
print("This is how it would look now: ")
print(b)
print()
print("Let's change the first element of the second row in B to 8")
b[1, :] = 8
print("This is how it would look now: ")
print(b)
print()

# What about initializing different types of arrays?
# 2 0s array in different dimensions
print("One dimension: ", np.zeros(2))
print()
print("Two dimensions: ", np.zeros((2,2)))
print()
print("Three dimensions: ", np.zeros(((2,2,2))))
print()
# Like zeros there is ones, but what about other numbers? We can use the full method
print("Two dimensios array composed by the element 99:", np.full((2,2), 99))
print()
# The difference with the full_like method is that the like use a previous built array as reference
print("Let's make an array like the A, but with the number 75:", np.full_like(a, 4))
print()
# We can also initialize an array of random numbers
print("This is a 2x2 array of random floats: ", np.random.rand(4,2))
print()
print("Or using A shape as reference: ", np.random.random_sample(a.shape))
print()
# If we only want intergers values
print("This is an array of random intergers between 1 and 10 in the A shape: ", np.random.randint(1,11 , size=a.shape))
print()
# What about an array of a certain shape? Use the identity:
print("This is an array of 3x3: ", np.identity(3))
print()
# There is also a repeat method, for example if we want to repeat array B 3 times:
print("This is how we repeat an array: ")
repeat_a = np.repeat(b, 3, axis=0)
print(repeat_a)
print()
# We are only initializing arrays here, so let's complicate it a bit
# Let's try to initialize a 5x5 array that has all the corners with a value of 1, the center element with a value of 5 and the remaining elements with a value of 0:
print("This is how we could initialize a 5x5 array with our problem from the comment without typing all elements:")
problem_array = np.ones((5,5))
problem_array[2,2] = 5
problem_array[1,1:4] = 0
problem_array[2,1] = 0
problem_array[2,3] = 0
problem_array[3,1:4] = 0
print()
print(problem_array)
print()
# But there is an easier way, we break it down:
problem_array_2 = np.ones((5,5)) # First create the full 5x5 array with all elements as 1
zeros = np.zeros((3,3)) # Then create a 3x3 middle array with all elements as 0
zeros[1,1] = 5  # And we modify the middle element to 5
problem_array_2[1:4, 1:4] = zeros
print("Same output with different code:")
print(problem_array_2)
print()
# Something to have due care with is when declararing two arrays are equal to each other, since by modifying one we will be modifying the other one. Declaring something is equal in NUMPY work both ways - Unless we declare array_b = array_a.copy()

# Getting started with mathematics in NUMPY
print("Mathematics in NUMPY")
math = np.array([2, 3, 4, 5])
print(math)
print()
print("We can use the + to add to each element of an array, for example let's add 2:", math + 2)
print()
print("We can use the - to subtract from each element of an array, for example let's subtract 2:", math - 2)
print()
print("We can use the * to multiply each element of an array, for example let's multiply by 2:", math * 2)
print()
print("We can use the / to divide each element of an array, for example let's divide by 2:", math / 2)
print()
print("We can use the ** to elevate each element of an array, for example let's elevate to the 2nd power:", math ** 2)
print()
print("We can get sin of each element of an array, for example:", np.sin(math))
print()
print("We can get cos of each element of an array, for example:", np.cos(math))
print()
print("The array remains unmodified, as each operation only exists in that function")
print()
math_2 = np.array([1, 2, 3, 4])
print("Let's make a new array: ", math_2)
print()
print("And we can play between arrays using operations as well: ", math+math_2)
print()
print("We can also use NUMPY array_min() / array_max() / array_mean() to obtain information about elements of an array, they are kind of self explanatory.")
print()

# NUMPY can also reorganize an array, changing shapes or stack for example
print("Reorganizing arrays")
print()
print("Changing shape for example we have an array of 4x4 and want it in 2x8")
before = np.identity(4)
print(before)
after = before.reshape(2,8)
print()
print("If we do a .reshape(2,8) this is what we will get:")
print(after)
print()
print("Stacking arrays")
v1 = np.array([0, 1, 2])
v2 = np.array([3, 4, 5])
print()
print(v1)
print("We want the array above and bellow to become one stacked array")
print(v2)
print()
print("Using np.vstack([arrayid1, arrayid2]) we get:")
print(np.vstack([v1, v2]))
print()
# Horizontal stacks work similarly to .vstack


# Loading external data in NUMPY
# fd = np.genfromtxt(_'insert path to file'_, delimiters='_indicate if any_')

# If the data is imported as float you can use the .astype('int') to transform it into interger

# Advanced indexing in NUMPY (Boolean, Masking and Advanced Index)
# 
# By running a filter like:
# fd > 15  will return with a boolean result, True or False, for each element.
# On the other hand, doing something like:
# fd[fd > 15] will return only the data where that condition is met.

# To find out if any element meets a condition we can use the np.any(fd > 15, axis=0) and this will return a boolean result.
# If we run np.all and the same () content we will get a different result ??

# Advanced indexing
# Indexing with a list
# Let's say you want to retrieve the value of certain elements (let's say the first and last) from the filedata (fd), you can just index with the following logic:
# fd[[1, -1]]
# fd[[>15]]

# Well, there is a lot to learn, but this was just an afternoon of exercises. No need to know these and more by heart, I believe it comes naturaly.
