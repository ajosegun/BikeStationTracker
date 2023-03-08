import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import os

import helper

list_of_cities_from_api = helper.get_all_cities()

user_city = helper.get_user_city_from_ip()
default_user_city = "Paris"

if user_city == "Could not get your location.":
    st.write(f"Could not get your location, using default location: Select a city on the left")
    user_city = default_user_city

elif user_city not in list_of_cities_from_api:
    ## Set default user city
    st.subheader(f"Bike Data not available for detected city: {user_city}, using default location")

    user_city = default_user_city

selected_city = st.sidebar.selectbox("Select or Type your city", 
                                     list_of_cities_from_api,
                                     index=list_of_cities_from_api.index(user_city))

list_of_stations_from_api = helper.get_list_of_stations_names_in_city(selected_city)
station_name = st.sidebar.selectbox('Select or Type your station name', 
                                    list_of_stations_from_api,
                                    )

st.subheader(f"Showing Bike Map for selected city (you can change this on the right): {selected_city}")

live_city_data = helper.get_available_stations(selected_city)
fig_map = helper.show_map(live_city_data, selected_city)

station_data = helper.get_location_data(station_name, live_city_data)
fig_bar = helper.show_bar_chart(station_data)



# Use st.plotly_chart() to display the map
st.plotly_chart(fig_map, height=1080, width=800)
st.plotly_chart(fig_bar, height=1080, width=800)








