import streamlit as st
import pandas as pd
# import numpy as np
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import mysql.connector
# from datetime import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Aftab_9696",
    database = "project1"
)
cursor = connection.cursor()

#0____________________________________________________________________________________________
cursor.execute("SELECT routes FROM rb_root_links")

df = cursor.fetchall()
df=pd.DataFrame(df)
st.sidebar.image("D:\\GUVI\\visual_studio\\Red_bus_v0.1\\Red_bus_data_scrapping\\th.jpg")
xan = st.sidebar.selectbox('select Route', df)

time_filters = ['Filter by Departure Time', 'Filter by Reaching Time']
filter_selec = st.sidebar.radio('Select Filter',time_filters)

cursor.execute("SELECT DISTINCT(Bus_Type) FROM bus_details")
bus_type = cursor.fetchall()
bus_type = pd.DataFrame(bus_type)

depot = 'RTC' 
#1________________________________________________________________________________________________

if filter_selec == 'Filter by Departure Time':
    with st.form(key = 'bus details'):
        st.subheader('Selct Bus Details')
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
                dep_time_selector = st.selectbox('Departure Time',['Before','After'])
                dep_time = st.time_input('')
        with c3:
            rating = st.selectbox('Start Rating', [1, 2, 3, 4, 5])
        with c4:
            seats = st.number_input('Seats Availability', 1, 100, 1)
        with c2:
            bus_depo = st.selectbox('Operator',['RTC', 'Private','All'])
            
        bustype = st.selectbox('Bus Type', bus_type)
        
        if submit_button := st.form_submit_button(label='Submit'):
            st.text('Submitted')

    #rtc bus querry before time
    query1 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name like '%{depot}%' AND
        Depart_Time <= '{dep_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""
    
    #private bus querry before time
    query2 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name NOT LIKE '%{depot}%' AND
        Depart_Time <= '{dep_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""
    
    #all bus querry before time
    query3 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Depart_Time <= '{dep_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""

    #rtc bus querry after time
    query4 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name like '%{depot}%' AND
        Depart_Time >= '{dep_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""   

    #all bus querry after time
    query5 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name NOT LIKE '%{depot}%' AND
        Depart_Time >= '{dep_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""

    #private bus querry after time
    query6 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Depart_Time >= '{dep_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""

            
    if dep_time_selector == 'Before' and bus_depo == 'RTC':
        query = query1

    elif dep_time_selector == 'Before' and bus_depo == 'Private':
        query = query2

    elif dep_time_selector == 'Before' and bus_depo == 'All':
        query = query3
        
    elif dep_time_selector == 'After' and bus_depo == 'RTC':
        query = query4   

    elif dep_time_selector == 'After' and bus_depo == 'Private':
        query = query5
    
    else:
        query = query6
        
    cursor.execute(query)
    
#2___________________________________________________________________________________________________________
else:
    with st.form(key = 'bus details'):
        st.subheader('Selct Bus Details')
        
        c1, c2, c3, c4 = st.columns(4)
        
        with c1:
                #before and after arrival time selection
                arr_time_selector = st.selectbox('Reach Time',['Before','After'])
                arr_time = st.time_input('')
        with c3:
            rating = st.selectbox('Start Rating', [1, 2, 3, 4, 5])
        with c4:
            seats = st.number_input('Seats Availability', 1, 100, 1)
        with c2:
            bus_depo = st.selectbox('Operator',['RTC', 'Private','All'])
        
        bustype = st.selectbox('Bus Type', bus_type)
        
        if submit_button := st.form_submit_button(label='Submit'):
            st.text('Submitted')

    #rtc bus querry before time
    query1 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name like '%{depot}%' AND
        Reach_Time <= '{arr_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""
    
    #private bus querry before time
    query2 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name NOT LIKE '%{depot}%' AND
        Reach_Time <= '{arr_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""
    
    #all bus querry before time
    query3 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Reach_Time <= '{arr_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""

    #rtc bus querry after time
    query4 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name like '%{depot}%' AND
        Reach_Time >= '{arr_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""   

    #all bus querry after time
    query5 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Bus_Name NOT LIKE '%{depot}%' AND
        Reach_Time >= '{arr_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""

    #private bus querry after time
    query6 = f"""SELECT * FROM bus_details WHERE
        Route_Name = '{xan}' AND
        Reach_Time >= '{arr_time}' AND
        Star_Rating>={rating} AND
        Bus_Type = '{bustype}' AND
        Seats_Available >= {seats};"""
    
    
    
    if arr_time_selector == 'Before' and bus_depo == 'RTC':
        query = query1

    elif arr_time_selector == 'Before' and bus_depo == 'Private':
        query = query2

    elif arr_time_selector == 'Before' and bus_depo == 'All':
        query = query3
        
    elif arr_time_selector == 'After' and bus_depo == 'RTC':
        query = query4   

    elif arr_time_selector == 'After' and bus_depo == 'Private':
        query = query5
    
    else:
        query = query6

    cursor.execute(query)
#______________________________________________________________________________________________________________

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
    if min_price != max_price:
        price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))
        filter_data = data[(data["Price"] >= price_range[0]) & (data["Price"] <= price_range[1])]
    else:
        filter_data = data
        
    no_bus = filter_data['Bus Name'].count()
    #if no_bus >0:
    st.dataframe(filter_data, hide_index=True)
    st.subheader(f"{no_bus} Buses Found :thumbsup:")
    st.write("First Bus Depart At", filter_data['Departure Time'].min())
    st.write("Last Bus Depart At", filter_data['Departure Time'].max())
else:
        st.write('No Buses Found. Try Other Routes')
