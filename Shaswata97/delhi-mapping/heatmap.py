import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import itertools

df=pd.read_excel('Delhi_mapping.xlsx')
X=pd.DataFrame(df)
X.drop(['name','community mapped by name','community mapped by surname'],1,inplace="True");
for i in range(len(X)):
	comm=eval(X.iloc[i]['community'])
	comm=[str(x) for x in comm]   #converting string to list
	X.iloc[i]['community']=comm   #storing the communities as a list.

stn=np.unique(np.array(X['Polling Station Number']))
com=sum(X['community'],[])  #converting lists of lists into a single lists containing all communities
com=np.unique(np.array(com))

mapX=pd.DataFrame(columns=com, index=stn)   #mapX[i][j] will store the the number of people belonging to j-th community in i-th station
for i in range(len(stn)):
	for j in range(len(com)):
		mapX.iloc[i][j]=0  # initializing the frequencies with zero

print("Generating heatmap")
#counting the frequencies
for i in range(len(X)):
	st=X.iloc[i]['Polling Station Number']     #denotes the polling station number
	for j in X.iloc[i]['community']:
		mapX.loc[st][j]+=1

print("Heatmap ready!")
mapX.fillna(value=0, inplace=True)   #filling all NaN values which pose problems in heatmap generation and future calculations
img=sns.heatmap(mapX)
loc, labels=plt.xticks()
loc2, labels2=plt.yticks()
img.set_xticklabels(labels, rotation=90)
img.set_yticklabels(labels2, rotation=0)
img.figure.tight_layout()
img.figure.savefig('heatmap.png')
plt.show()
