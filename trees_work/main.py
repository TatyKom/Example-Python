"""
Trees
"""
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("trees.csv")
df = df.sort_values(by="Girth")
plt.plot(list(df['Girth']))
plt.show()
plt.hist(df.sort_values(by="Girth")['Girth'], bins=10)
plt.show()
df = df.sort_values(by="Height")
plt.plot(list(df['Height']))
plt.hist(df.sort_values(by="Height")['Height'], bins=10)
plt.show()
df = df.sort_values(by="Volume")
plt.plot(list(df['Volume']))
plt.hist(df.sort_values(by="Volume")['Volume'], bins=10)
plt.show()
