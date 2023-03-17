## Bike Station Tracker
Bike Station Tracker enables bikers to view information about bike sharing stations in real time. The application uses data provided by the [Citybik API](http://api.citybik.es/v2/networks)

It utilizes the power of Python and the simplicity of Streamlit and Plotly to provide a user-friendly interface for users to interact with the data in form of maps and visualizations. Data is retrieved from the Citybik API.

[Check more on Medium](https://medium.com/@ajosegun_/real-time-dashboard-in-python-b8c9a9c4e050)

## Demo
[Bike Station Tracker](https://ajosegun-bikestationtracker.streamlit.app/) Note that it might take a while to load the first time.

## Features
The Bike Station Tracker application provides the following features:

1. Real-time bike station data: The application retrieves real-time data from the Citybik API, allowing users to view up-to-date information about the number of available bikes and bike stands at each station.

2. Interactive map: The application displays a map of the detected (or selected) location, allowing users to easily locate bike sharing stations and view information about them.

3. Search functionality: Users can search for bike sharing stations by name using the search box in the top left corner of the page. The application will display all stations whose name contains the search term.

4. Responsive design: The application is designed to be responsive, meaning it will display properly on devices of all sizes, from desktop computers to mobile phones.

Visualizations
1. Live Map (Dashboard)

2. Bar Chart - for selected station

3. Pie Chart - for selected station

## Requirements
Python 3.6 or higher Streamlit Pandas Plotly 

## Installation
To install the required packages, run the following command: pip install -r requirements.txt

## Usage
To run the application, navigate to the root directory of the project in the terminal and run the following command:

streamlit run app.py

This will start the application and launch a local server at http://localhost:8501/ in your web browser.

## Conclusion
The Bike Station Tracker is a useful web application that retrieves data from [Citybikes API](http://api.citybik.es/v2/networks) and allows users to view information about bike sharing stations in cities around the world. 
It provides an interactive map and search functionality for easy navigation and filtering of stations. With its easy installation process and responsive design, the Bike Station Tracker is a valuable tool for anyone looking to access real-time information about bike sharing stations.
