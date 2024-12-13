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
st.sidebar.image("D:\\GUVI\\visual studio\\th.jpg")
xan = st.sidebar.selectbox('select state transport corp', df)

cursor.execute("SELECT * FROM bus_details WHERE Route_Name = %s", (xan,))
data=cursor.fetchall()
data = pd.DataFrame(data, columns = ['Bus ID', 'Bus Name','Type', 'Departure Time', 'Duration', 'Reaching Time', 'Star Rating', 'Price', 'Seats','Route'])

data["Departure Time"] = data["Departure Time"].apply(lambda x: str(x).split(' ')[-1])
data["Reaching Time"] = data["Reaching Time"].apply(lambda x: str(x).split(' ')[-1])

no_bus = data['Bus Name'].count()
if no_bus >0:
    st.dataframe(data, hide_index=True)
    st.subheader(f"{no_bus} Buses Found :thumbsup:")
else:
    st.write('No Buses Found. Try Other Routes')

