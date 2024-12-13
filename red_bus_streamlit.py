import streamlit as st
import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aftab1234",
    database = "project1"
)
cursor = connection.cursor()

st.subheader("Your search will appear here :hourglass:")
cursor.execute("SELECT routes FROM rb_root_links")

df = cursor.fetchall()
df=pd.DataFrame(df)
st.sidebar.image("D:\\GUVI\\visual studio\\v0.1\\th.jpg")
xan = st.sidebar.selectbox('select state transport corp', df)

cursor.execute("SELECT * FROM bus_details WHERE Route_Name = %s", (xan,))
d1=cursor.fetchall()
d1 = pd.DataFrame(d1, columns = ['Bus ID', 'Bus Name','Type', 'Departure Time', 'Duration', 'Reaching Time', 'Star Rating', 'Price', 'Seats','Route'])
#hide the bus route name from the display box
data = d1[['Bus ID', 'Bus Name','Type', 'Departure Time', 'Duration', 'Reaching Time', 'Star Rating', 'Price', 'Seats']]
data["Departure Time"] = data["Departure Time"].apply(lambda x: str(x).split(' ')[-1])
data["Reaching Time"] = data["Reaching Time"].apply(lambda x: str(x).split(' ')[-1])

#price selection
if data.empty == False:
    st.sidebar.markdown("#### PRICE RANGE")
    min_price = data['Price'].min()  # Adjusted minimum price
    max_price = data['Price'].max()  # Adjusted maximum price
    filter_price = pd.DataFrame()
    price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))
    filter_data = data[(data["Price"] >= price_range[0]) & (data["Price"] <= price_range[1])]

    no_bus = filter_data['Bus Name'].count()
    #if no_bus >0:
    st.dataframe(filter_data, hide_index=True)
    st.subheader(f"{no_bus} Buses Found :thumbsup:")
    st.write("First Bus Depart At", filter_data['Departure Time'].min())
    st.write("Last Bus Depart At", filter_data['Departure Time'].max())
else:
        st.write('No Buses Found. Try Other Routes')
