import streamlit as st
import folium
import geopandas
import pandas as pd

from streamlit_folium import st_folium # New import

st.set_page_config(layout="wide")

st.title('Simple Map Example')

# Read in our dataframe
# Notice here I'm just loading it from a repository - we could also load it from local storage
# as long as the same data will be available in the same relative position when we deploy our web app
gp_list = pd.read_csv("https://github.com/hsma-programme/h6_3b_advanced_qgis_mapping_python/raw/main/h6_3b_advanced_qgis_and_mapping_in_python/example_code/gp_surgery_locations_plus_patient_list_size.csv")

###########################
# Create the map in Folium
###########################
# This is no different to usual!
# In fact, this is the code from the HSMA geographic modelling book (module 3)
# https://hsma-programme.github.io/hsma6_geographic_optimisation_and_visualisation_book/python_geopandas_folium_point_data.html

gp_list_gdf = geopandas.GeoDataFrame(
    gp_list, # Our pandas dataframe
    geometry = geopandas.points_from_xy(
        gp_list['result_eastings'], # Our 'x' column (horizontal position of points)
        gp_list['result_northings'] # Our 'y' column (vertical position of points)
        ),
    crs = 'EPSG:27700' # The dataset is currentl in EPSG:27700 (northings/eastings)
    )

# Convert to 4326 (lat/long) for working with Folium as this is the format it understands
# This will convert all of our coordinates to latitude and longitude
gp_list_gdf = gp_list_gdf.to_crs('EPSG:4326')

# Filter out instances with no 'list' (e.g. things like specialist clinics)
gp_list = gp_list[~gp_list['Total List Size'].isna()]

# reduce to the southwest to not overload Folium
xmin, xmax = -6.449974,-2.717735
ymin, ymax =  49.814737,51.246969
gp_list_gdf_sw = gp_list_gdf.cx[xmin:xmax, ymin:ymax]

# Filter out instances with no geometry
gp_list_gdf_sw = gp_list_gdf_sw[~gp_list_gdf_sw['geometry'].is_empty]

# Create a geometry list from the GeoDataFrame
geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in gp_list_gdf_sw.geometry]

# reduce to the southwest to not overload Folium
xmin, xmax = -6.449974,-2.717735
ymin, ymax =  49.814737,51.246969
gp_list_gdf_sw = gp_list_gdf.cx[xmin:xmax, ymin:ymax]

gp_map_tooltip = folium.Map(
    location=[50.7, -4.2],
    zoom_start=8,
    tiles='openstreetmap',
    )

# This will loop through the list of x/y coordinates we've made
# The first pair of coordinates will return i = 0, coordinates = (latitude, longitude)
# The second pair will return return i = 1, coordinates = (latitude, longitude)
# and so on and so forth
for i, coordinates in enumerate(geo_df_list):

    gp_map_tooltip = gp_map_tooltip.add_child(
        folium.Marker(
            location=coordinates,
            # Folium in streamlit sometimes seems to have issues with the default provided markers;
            # using fontawesome markers instead is an easy way to solve this problem
            icon=folium.Icon(icon="user-md", prefix='fa', color="black"),
            # Here I've slightly enhanced the tooltip with an f string to display both the list
            # size and the practice name
            # Remember here that the list we are iterating through is in the same order as our main
            # dataframe! So we can use the variable 'i' to access the row that matches the coordinates
            # we are plotting from our list, which allows us to pull out useful things like the
            # practice name and the practice list size
            # <br/> is just a bit of HTML that means the text after it will start on a new line
            # You often have to use this in web contexts instead of \n
            tooltip=f"{gp_list_gdf_sw['name'].values[i]}<br/>List Size: {gp_list_gdf_sw['Total List Size'].values[i]:.0f}"
            )
     )

###################################
# KEY NEW BIT
###################################
# Display the map
####################################
# This is the only code we need to add in to display the map in Streamlit!
# We can pass in use_container_width=True to ensure it uses the maximum available space
st_folium(gp_map_tooltip, use_container_width=True)
