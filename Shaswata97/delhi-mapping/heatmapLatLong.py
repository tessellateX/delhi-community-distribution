import numpy as np
from ipywidgets.embed import embed_minimal_html
#from geopy.geocoders import Nominatim
import matplotlib
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
import pandas as pd
import googlemaps
import gmaps

df=pd.read_csv('Delhi_mapping.csv')
df.drop(['Id','name','community mapped by name','community mapped by surname'],1,inplace=True)
for i in range(len(df)):
    comm=eval(df.iloc[i]['community'])
    comm=[str(x) for x in comm]    #converting string to list
    df.iloc[i]['community']=comm   #storing the communities as a list.

#def findLatLong():
#    #Function to find the location
#    global df
    #Finding location using geopy
#    geolocator=Nominatim()
#    df['latitude']=0
#    df['longitude']=0
#    for i in range(len(df)):
#        stn=df.iloc[i]['Polling Station Number']
#        location = geolocator.geocode(stn)
#        df.ix[i,'latitude']= location.latitude
#        df.ix[i,'longitude']=location.longitude

def stationUnique():
    #Function to find unique station names
    stations=list(set(df['Polling Station Number']))
    print(len(stations))
    return stations

def communityUnique():
    # Function to determine the unique communities
    com=sum(df['community'],[])  #converting lists of lists into a single lists containing all communities
    com=np.unique(np.array(com))
    return com


def countCommunitites():
    # Function to count the communitites
    global comsize
    comsize=len(communityUnique())

mapX=pd.read_csv('map_data.csv')
print(mapX.head())

def plotMap():
    #stn=stationUnique()
    #comm=communityUnique()
    #col=comm.tolist()
    #col.append('longitude')
    #col.append('latitude')
    #mapX=pd.DataFrame(0.0,columns = col, index=stn)
    #mapX['latitude']=0.5
    #mapX['longitude']=0.5
    #geolocator=Nominatim()
    #gmaps=googlemaps.Client('AIzaSyAKjT0JFQOrn8wicV3tRu3WYKqKhUDPSG4')
    
    #finding the latitude and longitude of polling stations
    #j=0
    #for i in range(len(stn)):
    #    stn_i=stn[i]	
    #    #location = geolocator.geocode(stn_i)
    #    stn_geo=gmaps.geocode(stn_i)
    #    #print(stn_geo)
    #    if(len(stn_geo)!=0):
    #        j=j+1
    #        lat = stn_geo[0]["geometry"]["location"]["lat"]
    #        lon = stn_geo[0]["geometry"]["location"]["lng"]
    #        print(lat,lon)
    #        mapX.at[stn_i,'latitude']= lat
    #        mapX.at[stn_i,'longitude']=lon
    #    else:
    #        print(stn_i)
    #        continue
    #print("Locations found",(j))
        
    #finding the frequencies of communities
    #for i in range(len(df)):
    #    stn_i=df.iloc[i]['Polling Station Number']
    #    for j in df.iloc[i]['community']:
    #        mapX.at[stn_i,j]=mapX.loc[stn_i][j]+1
    #mapX.to_csv('map_data.csv',sep='\t') 
    print("Table created!")
    maxLat=np.amax(mapX['latitude'])
    print("max lat = ",(maxLat))
    minLat=np.amin(mapX['latitude'])
    print("min lat = ",(minLat))
    maxLong=np.amax(mapX['longitude'])
    print("max long = ",(maxLong))
    minLong=np.amin(mapX['longitude'])
    print("min long = ",(minLong))
    
    #creating basemap object
    print("Creating basemap")
    #img = Basemap(projection='merc',lat_0=28,lon_0=76,llcrnrlon=74,llcrnrlat=25,urcrnrlon=78,urcrnrlat=30)
    #img.drawcoastlines()
    #img.fillcontinents(color='coral')
    #img.drawcountries()
    #img.drawstates()
    
    #finding unique latitudes and longitudes
    #lats=np.array(list(set(mapX['latitude'])))
    #lons=np.array(list(set(mapX['longitude'])))
        
    #modifying data into size (len(lats) , len(lons))
    #mapim=pd.DataFrame(0,index=lats, columns=lons)
    #for i in range(len(mapX)):
    #    mapim.at[mapX.iloc[i]['latitude'] , mapX.iloc[i]['longitude']]=mapX.iloc[i][col[2]] #bengali community
    #print(mapim)
    
    #np.append(lats,maxLat+1)
    #np.append(lons,maxLong+1)
    #X,y=img(lons,lats)

    #extra arguments
    #cmapx=plt.get_cmap('rainbow')
    #cmapx.set_under('white')
    
    #im=img.pcolormesh(X,y,mapim,cmap=cmapx)
    #img.colorbar(im, extend='min')
    #img.drawparallels(np.arange(28,30,0.5), labels=[False, True, False, True])
    #img.drawmeridians(np.arange(76.0,78.0,0.5), labels=[True, False, True, False])
    
    #gmaps=googlemaps.Client('AIzaSyAKjT0JFQOrn8wicV3tRu3WYKqKhUDPSG4')
    gmaps.configure('AIzaSyBwEyjaABv6E1VJK3P_GKmMrvCIs8QEBJI')
    img=gmaps.figure()
    img.add_layer(gmaps.heatmap_layer(mapX[['latitude','longitude']] , weights=mapX['bengali']))
    embed_minimal_html('mapping.html' , views=[img])
    return img

img=plotMap()