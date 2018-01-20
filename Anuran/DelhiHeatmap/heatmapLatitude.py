# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:16:24 2018

@author: ANURAN
"""
import numpy as np
from ipywidgets.embed import embed_minimal_html
from matplotlib import pyplot as plt
from googlemaps import Client
import pandas as pd
from mpl_toolkits.basemap import Basemap
import googlemaps
import gmaps

df=pd.read_csv('Delhi_mapping.csv')
df.drop(['Id','name','community mapped by name','community mapped by surname'],1,inplace=True)

def findUniqueComm():
    # Function to find the unique communitites
    global df
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
    return communities

def findLat(addr):
    # Function to find latitude and longitude using google maps API
    gmaps = Client(key='AIzaSyAr6MafwMH3Anrx_aJNb3_y7KrWKlCcNOA')
    geocode_result = gmaps.geocode(addr)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    return [lat,lon]

community=findUniqueComm()
#stations=list(set(df['Polling Station Number'])) #list of all stations without repition
#count=pd.DataFrame(columns=community,index=stations)#count.loc[i][j] gives strength of community j in station i
#count.astype(float)

def countComm():
    #Function to find the count of each community
    global df
    global count
    global stations
    global community
    for i in stations: #init all count to zero
        for j in community:
            count.loc[i][j]=0

    for i in range(len(df)):
        s=df.iloc[i]['Polling Station Number']
        for j in df.iloc[i]['community']: #traversing through list of communities of the station
            count.loc[s][j]+=1
    
    count.drop([''],1,inplace=True)
    count.fillna(value=0, inplace=True)
    
def fillLatLong():
    # Function to fill latitude and longitude
    global community
    global stations
    global count
    count['lat']=0.5
    count['lon']=0.5
    count.lat.astype(float)
    count.lon.astype(float)
    for i in stations:
        print(findLat(i)[0])
        count.at[i,'lat']=float(findLat(i)[0])
        count.at[i,'lon']=float(findLat(i)[1])

#countComm()
#fillLatLong()
#count.to_csv('count.csv',sep=',',encoding='utf-8')
count=pd.read_csv('count.csv')
print(count.head())

def PlotMap():
    # Fucntion to create basemap
    global count
    global community
    
    gmaps.configure('AIzaSyBwEyjaABv6E1VJK3P_GKmMrvCIs8QEBJI')
# =============================================================================
#     m  = Basemap(projection='mill',llcrnrlon=min(count['lon']),llcrnrlat=min(count['lat']),urcrnrlat=max(count['lat']),urcrnrlon=max(count['lon']))   
#     m.drawstates()
#     m.drawcoastlines()
#     m.drawcounties()
# =============================================================================
    
    #Plotting the data
# =============================================================================
#     lon=np.array(count['lon'])
#     lat=np.array(count['lat'])
#     data=np.array(count['english'])
#     x,y = m(lon,lat)
#     m.scatter(x,y,data)
# =============================================================================
# =============================================================================
#     data = [(float(count.iloc[i]['lat']), float(count.iloc[i]['lon'])) for i in range(len(count))]
#     print(data)
#     gmaps.heatmap(data)
# =============================================================================
    locations=count[['lat','lon']]
    weight=count['english']
    fig = gmaps.figure()
    fig.add_layer(gmaps.heatmap_layer(locations, weights=weight))
    embed_minimal_html('export.html', views=[fig])
    return fig

fig=PlotMap()

    