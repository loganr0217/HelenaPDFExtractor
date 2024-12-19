import pandas as pd
import folium
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup

# Gets the coordinates of an address to search on google maps
def getCoordinatesFromAddress(address):
    coordinates = [39.3320792,-82.09839]

    try:
        
        URL = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?benchmark=4&address=" + address
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        # Get contents of first script to extract coordinates from
        test = soup.text[soup.text.find("Interpolated Longitude (X) Coordinates: ")+40:]
        test = test.split("\nTigerline ID:")[0]
        test = test.split("\nInterpolated Latitude (Y) Coordinates:")

        coordinates = [float(i) for i in test]
        coordinates = [coordinates[1], coordinates[0]]
        # coordinates = [float(i) for i in coordinates]
    
    except:
        print("Error with loading coordinates")

    return coordinates

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('../test.xlsx')

numHospitals = len(dataframe1["Mail Address"])

# Getting all full addresses from excel file
addresses = []
for i in range(numHospitals):
    address = dataframe1["Mail Address"][i] + ", " + dataframe1["City/State"][i]
    addresses.append(address)
    # print(address)


# Sample addresses **only used for testing**
# addresses = ["1600 Amphitheatre Parkway, Mountain View, CA", "Times Square, New York, NY"]

# Geocode addresses
locations = []
for address in addresses:
    location = getCoordinatesFromAddress(address)
    locations.append((location[0], location[1]))

# Create map
my_map = folium.Map(location=locations[0], zoom_start=5)

# Add markers with icons
for location in locations:
    icon = folium.Icon(color="blue", icon="home", prefix="fa")
    folium.Marker(location, icon=icon).add_to(my_map)

# Save the map
my_map.save("map_with_icons.html")
