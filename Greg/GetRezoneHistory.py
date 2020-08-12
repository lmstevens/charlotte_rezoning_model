# Dependencies
import requests
import json
import pandas as pd
import types

# from geojson_utils import centroid # does not like decimals

def getCentralPoint(feature):
    lat = 0.0
    lng = 0.0
    record_count = 0
    for coordinates in feature['geometry']['coordinates']:
        for coordinate in coordinates:
            if not all(isinstance(x, list) for x in coordinate):
                lng += coordinate[0]
                lat += coordinate[1]
                record_count+= 1
            else:
                for coordinate2 in coordinate:
                    lng += coordinate2[0]
                    lat += coordinate2[1]        
                    record_count+= 1        

    centroid = {}
    centroid['lng'] = lng / record_count
    centroid['lat'] = lat / record_count

    return centroid

url = 'https://opendata.arcgis.com/datasets/19c8803ab1214b21859127d463034520_23.geojson'

geo_data = requests.get(url).json()

for feature in geo_data['features']:
    feature['centroid'] = getCentralPoint(feature)


rezoning_history_df = pd.DataFrame(geo_data['features'])
print(rezoning_history_df.head())

# Print the json
#print(geo_data)
