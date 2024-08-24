import folium
from geopy.distance import geodesic
#pip install folium geopy

# Coordinates for unique locations
syd_airport = (-33.9399, 151.1753)
locations = {
    "Sydney Opera House (Opera House Tour, NYE Gala, Fireworks)": (-33.8568, 151.2153),
    "Sydney Harbour Bridge (BridgeClimb)": (-33.8523, 151.2108),
    "Bondi Beach": (-33.8908, 151.2743),
    "Manly Beach": (-33.7969, 151.2874),
    "Circular Quay to Manly Ferry": (-33.8615, 151.2111),
    "Botanic Garden Foundation and Friends NYE Picnic": (-33.8642, 151.2166)
}

# Create a map centered around Sydney
sydney_map = folium.Map(location=[-33.8688, 151.2093], zoom_start=13)

# Add the airport marker
folium.Marker(syd_airport, popup='Sydney Airport (SYD)', icon=folium.Icon(color='red')).add_to(sydney_map)

# Add markers for each unique location and calculate distance from the airport
for name, coord in locations.items():
    distance = geodesic(syd_airport, coord).km
    folium.Marker(
        coord,
        popup=f"{name}\nDistance from SYD: {distance:.2f} km",
        icon=folium.Icon(icon="info-sign")
    ).add_to(sydney_map)

# Save the map as an HTML file
sydney_map.save('sydney_map_consolidated.html')

