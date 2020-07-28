import pandas as pd
import numpy as np 

df = pd.read_csv('/Users/Konrad/Desktop/python/Hangman/1000mostpopularwords.csv')
  
x = df.values.tolist()
print(x)