import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./pandas practice/product_ratings_january_2022.csv')
print(df)

df = df.set_index('Date')

plot = df.plot()
print(plot)