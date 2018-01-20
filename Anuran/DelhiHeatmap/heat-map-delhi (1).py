import numpy as np
import pandas as pd
import seaborn as sns; sns.set()
from matplotlib import pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
df=pd.read_csv("Delhi_mapping.csv")

df.drop(['Id','name','community mapped by name','community mapped by surname'],1,inplace=True)



for i,items in enumerate(df['community']):#loops to convert the string to list form in df[community]
    items=items[1:-1].split(',')
    c=[] #c temporarily stores the list of communities in the station
    for j in items:
        j=j.strip().strip("'").strip()
        c=c+[j]
    df.iloc[i]['community']=c #replacing the string with corresponding list

communities=[] #list of all communities without repition
for i in df['community']:
    communities=list(set(communities+i)) #appends the current communities which have not yet been added

print(communities)
stations=list(set(df['Polling Station Number'])) #list of all stations without repition


count=pd.DataFrame(columns=communities,index=stations)#count.loc[i][j] gives strength of community j in station i

for i in stations: #init all count to zero
    for j in communities:
        count.loc[i][j]=0

for i in range(len(df)):
    s=df.iloc[i]['Polling Station Number']
    for j in df.iloc[i]['community']: #traversing through list of communities of the station
        count.loc[s][j]+=1

count.drop([''],1,inplace=True)
count.fillna(value=0, inplace=True)
print (count)
#count2=np.array(count)
#print(count2)
ax = sns.heatmap(count)
x=plt.gca().xaxis

for item in x.get_ticklabels():
    item.set_rotation(90)

y=plt.gca().yaxis

for item in y.get_ticklabels():
    item.set_rotation(0)
plt.show()
