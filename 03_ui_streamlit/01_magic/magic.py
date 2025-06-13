# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''
import streamlit as st

import pandas as pd
df : pd.DataFrame = pd.DataFrame({'col1': [1,2,3],'col2':list('xyz')})
df  # 👈 Draw the dataframe


x : int = 100

'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)

fig  # 👈 Draw a Matplotlib chart

'# HELLO WORLD!'

# hello world
'''
# DOCUMENT TITLE

This is some _markdown_.
#underscore around a word makes it italized
'''