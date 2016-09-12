#!/usr/bin/env python
"""
In this mission, you'll learn the fundamentals of geographic coordinate systems and how to work with
the Basemap library to plot geographic data points on maps. You'll be working with flight data from
the openflights website. Here's a breakdown of the files we'll be working with and the most pertinent
columns from each dataset:
    airlines.csv - data on each airline
        country - where the airline is headquartered
        active - if the airline is still active
    airports.csv - data on each airport
        name - name of the airport
        city - city the airport is located
        country - country the airport is located
        code - unique airport code
        latitude - latitude value
        longitude - longitude value
    routes.csv - data on each flight route
        airline - airline for the route
        source - starting city for the route
        dest - destination city for the route
"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

airlines = pd.read_csv('../data/airlines.csv')
airports = pd.read_csv('../data/airports.csv')
routes  = pd.read_csv('../data/routes.csv')

# Enable interactive mode so plt.show() won't block
plt.ion()

# Customizing the plot using Matplotlib
fig = plt.figure(figsize=(15,20))
ax = fig.add_subplot(1,1,1)
ax.set_title('Scaled Up Earth With Coastlines and Airports')

# Create a new Basemap instance using the Mercator projection and desired edges
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

# Convert from Series objects to List objects since Basemap conversion won't work directly with Series
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()

# Converting From Spherical To Cartesian Coordinates
x, y = m(longitudes, latitudes)

# Display original longitude values
print(longitudes[0:5])
# Display original latitude values
print(latitudes[0:5])
# Display x-axis coordinates
print(x[0:5])
# Display y-axis coordinates
print(y[0:5])

# Generating A Scatter Plot
m.scatter(x, y, s=1)

# Customizing the plot using Basemap - draw in coastlines
m.drawcoastlines()

# Show the plot
plt.show()


# Create a geo_routes DataFrame contains the latitude and longitude values corresponding to the
# source and destination airports for each route.  Latitude and longitude for each airport is in
# the airports DataFrame.
airport_locs = airports[['iata', 'latitude', 'longitude']]
geo_routes = pd.merge(routes, airport_locs, left_on='source', right_on='iata')
columns = list(geo_routes.columns)
columns[-2:] = ['start_lat', 'start_lon']
geo_routes.columns = columns
del geo_routes['iata']
geo_routes = pd.merge(geo_routes, airport_locs, left_on='dest', right_on='iata')
columns = list(geo_routes.columns)
columns[-2:] = ['end_lat', 'end_lon']
geo_routes.columns = columns
del geo_routes['iata']


## Great Circles
fig = plt.figure(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

def create_great_circles(df):
    for index, row in df.iterrows():
        start_lon = row['start_lon']
        start_lat = row['start_lat']
        end_lon = row['end_lon']
        end_lat = row['end_lat']

        if abs(end_lat - start_lat) < 180 and abs(end_lon - start_lon) < 180:
            m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat, linewidth=1)

dfw = geo_routes[geo_routes['source'] == 'DFW']
create_great_circles(dfw)
plt.show()
