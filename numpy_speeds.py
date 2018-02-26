#==============================================================================
# Illustration of Python speed differences: For loop vs. numpy vectorization
# by Andrew Chamberlain, Ph.D.
# achamberlain.com
#==============================================================================

import numpy as np
import time
from math import log10 as log10
import matplotlib.pyplot as plt
import random

n = 100000 # Sample of rows to process.
seconds = [] # Empty list to computing times.

l1 = list(np.random.uniform(low=1.0, high=100.0, size=n)) # Create simple list. 

len(l1) # Size of l1.
l1[:10] # First 10 rows of l1. 

a1 = np.array(l1) # Create numpy array. 

a1.shape # Dimensions of a1. 
type(a1) # Data type for a1. 

l2 = [] # Empty list to append logged items into.

# Time to calculate n logs using a for loop. 
t1 = time.time()
for i in l1:
    l2.append(log10(i))
t2 = time.time()
print(format(t2-t1))
seconds.append(t2-t1)

# Time to calculate n logs using a vectorized numpy array. 
t1 = time.time()
a2 = np.log10(a1)
t2 = time.time()
print(format(t2-t1))
seconds.append(t2-t1)

# Bar chart of processing times. 
plt.figure(figsize=(5,3))
plt.ylabel("Time in seconds",fontsize=12)
plt.xlabel("Operation Type",fontsize=14)
plt.grid(True)
plt.bar(left=[1,2],height=seconds, align='center',tick_label=['For Loop','Numpy Vector'])
