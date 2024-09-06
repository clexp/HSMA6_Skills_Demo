#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of how numpy speed up computation.

For scientific applications you should aim to 
1. use numpy arrays over lists where possible
2. eliminate loops and use numpy built in functions and array operations 
(as these are written in C.)
"""

# Copy and paste each block to the console to run


#%%
import numpy as np

#%% 
#Example 1
# Lists versus arrays

# These will generate a Python list and a NumPy array, both consisting of
# numbers from 0 to 999999 (a million values)
python_list = list(range(1000000))
numpy_array = np.arange(1000000)

#%%
#baseline
# Let's time how long it takes to add up all the numbers in the Python list
%timeit sum(python_list)
# ms = millisecond (1 thousandth of a second) 
# µs = microsecond (1 millionth of a second)

#%%
#high performance
# Now let's time how long it takes to add up all the numbers in the NumPy list
%timeit np.sum(numpy_array)
