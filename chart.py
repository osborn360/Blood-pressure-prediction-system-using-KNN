import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
    
data = pd.read_csv('BP dataset.csv')
df = pd.DataFrame(data)

customcmap =  ListedColormap(["crimson", "mediumblue", "darkmagenta"])

df['BP'] = df['SBP'] / df['DBP']

plt.scatter(x=df['Family history'], y=df['BP'], s=30, c=df['Family history'].astype('category'), cmap=customcmap)



# plt.scatter(x=data['Drinking'], y = df['BP'], c=df['target'], cmap='red')
plt.xlabel('Family history')
plt.ylabel('Blood pressure')
plt.show()

 