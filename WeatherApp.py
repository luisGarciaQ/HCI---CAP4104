import requests
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time, date

from dateutil.utils import today

st.set_page_config(
    page_title="API Weather Project",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'About': 'Welcome to my NASA Weather Project. Developed by Kenan Kaaki, Luis Garcia and Michelle [lastname]'
    }
)

geoAPI = 'http://api.openweathermap.org/geo/1.0/direct?q={}&limit=5&appid=5022999a570d8796faf45a5365c4c3b1'
weatherAPI = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=5022999a570d8796faf45a5365c4c3b1&units=imperial'
weatherIcon = 'http://openweathermap.org/img/wn/{}@2x.png'
five_days = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&cnt=5&appid=5022999a570d8796faf45a5365c4c3b1&units=imperial'


def get_lon_lat(country):
    #error message
    info = requests.get(geoAPI.format(country))
    print(info)
    if info:
        country_json = info.json()
        lat = country_json[0]["lat"]
        lon = country_json[0]['lon']
        print(lat, lon)
        get_weather(lat, lon)
    else:
        st.error('Error: City not found', icon="🚨")


def get_weather(lat, lon):
    #button, widget,
    Info = requests.get(weatherAPI.format(lat, lon))
    five_daysAPI = requests.get(five_days.format(lat, lon))
    weather_json = Info.json()
    print(weather_json)
    st.write(five_daysAPI.json())
    the_icon = weatherIcon.format(weather_json['weather'][0]['icon'])
    st.metric(label="Temperature", value=f"{round(weather_json['main']['temp'])}°C")
    st.image(the_icon)
    five_days_display(five_daysAPI.json())

def five_days_display(json):
    arr = []
    iterable = 0
    for num in json['list']:
        arr.append(str(num['main']['temp']))

    for i in arr:
        st.write("list test: " + i)



    df = pd.DataFrame(
        np.arr.randn(7, 6),
        columns=('col %d' % i for i in range(6)))

    st.dataframe(df)













st.title("API Weather Project")
st.header("Please input the information below")
input = st.text_input("Please write the country")

if st.button("Find"):
    get_lon_lat(input)

    # TEST CODE BELLOW
# 1  last 5 days history weather.


  # Same as st.write(df)

# 2 reflects data above
#st.checkbox("Use container width", value=False, key="use_container_width")  # 5 checkbox
#chart_data = pd.DataFrame(
  #  np.random.randn(20, 3),
  #  columns=['a', 'b', 'c'])

#st.line_chart(chart_data)

# Bar Chart
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
# 3 Map
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [51.5085, -0.1257],
    columns=['lat', 'lon'])

st.map(df)

# 4 Button Widget
if st.button('Say hello'):  # Event Listener on click
    st.write('Why hello there')
else:
    st.write('Goodbye')

# 6 Success & Info box

if st.button("Click for sucess box"):
    st.success("This is a success message")
    st.info("This is an information message")

# 7 Teext input,
date_started = st.date_input("Start date at FIU")
today = date.today().year
test = st.text_input("This is a text input")
st.number_input("This is a number input")
st.date_input("Please select a date", date.today())
