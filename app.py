import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import os

import helper

list_of_cities_from_api = helper.get_all_cities()

user_city = helper.get_user_city_from_ip()
# user_city = "Paris"

if user_city not in list_of_cities_from_api:
    ## Set default user city
    st.subheader(f"Bike Data not available for kkjjk detected city: {user_city}")

    user_city = "Paris"

selected_city = st.sidebar.selectbox("Select or Type your city", 
                                     list_of_cities_from_api,
                                     index=list_of_cities_from_api.index(user_city))

list_of_stations_from_api = helper.get_list_of_stations_names_in_city(selected_city)
station_name = st.sidebar.selectbox('Select or Type your station name', 
                                    list_of_stations_from_api,
                                    )

st.subheader(f"Showing Bike Map for default city: {selected_city}")

live_city_data = helper.get_available_stations(selected_city)
fig = helper.show_map(live_city_data, selected_city)
# Use st.plotly_chart() to display the map
st.plotly_chart(fig, height=600, width=800)








