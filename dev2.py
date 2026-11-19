import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
data = pd.read_csv("CountryData.csv") 
plt.hist(data) 
plt.xlabel("code") 
plt.ylabel("Total_personal_income") 
plt.show()