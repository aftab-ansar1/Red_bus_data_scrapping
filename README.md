## Contents
**1. Introduction**

**2. Business Use Cases:**

**3. Approach**

**4. Data Set Requirements & Explanation:**

**5. Functionality:**

------------------------------------------------------------------------------------------------------------------------
**1. Introduction**

  The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.


**2. Business Use Cases:**
  The solution can be applied to various business scenarios including:
  ●	Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
  ●	Market Analysis: Analyzing travel patterns and preferences for market research.
  ●	Customer Service: Enhancing user experience by offering customized travel options based on data insights.
  ●	Competitor Analysis: Comparing pricing and service levels with competitors.

**3. Approach**

  1.	Data Scraping:
    ●	Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.
  2.	Data Storage:
    ●	Store the scraped data in a SQL database.
  3.	Streamlit Application:
    ●	Develop a Streamlit application to display and filter the scraped data.
    ●	Implement various filters such as bustype, route, price range, star rating, availability.
  4.	Data Analysis/Filtering using Streamlit:
    ●	Use SQL queries to retrieve and filter data based on user inputs. //currently only user input is route selection//
    ●	Use Streamlit to allow users to interact with and filter the data through the application.

**4. Data Set Requirements & Explanation:**

  The scraped dataset for this project contains detailed information about bus services available on Redbus, covering various aspects critical to travelers and service providers. Here is a breakdown of the fields:
    1. Route Details:
      ●	Bus Routes Name: This field captures the start and end locations of each bus journey, providing crucial information about the routes serviced.
      ●	Bus Routes Link: Link for all the route details.
    2. Bus Details:
      ●	Bus Name: The name of the bus or the service provider, which helps in identifying the specific operator.
      ●	Bus Type (Sleeper/Seater/AC/Non-AC): This field specifies whether the bus is a sleeper or seater type, indicating the seating arrangements and comfort   level offered.
    ●	Departing Time: The scheduled departure time of the bus, essential for planning travel schedules.
    ●	Duration: The total duration of the journey from the departure point to the destination, helping passengers estimate travel time.
    ●	Reaching Time: The expected arrival time at the destination, allowing for better planning of onward travel or activities.
    ●	Star Rating: A rating provided by passengers, indicating the quality of service based on factors such as comfort, punctuality, and staff behavior.
    ●	Price: The cost of the ticket for the journey, which can vary based on factors like bus type and demand.
    ●	Seat Availability: The number of seats available at the time of data scraping, giving real-time insight into the occupancy levels.
  Database Schema:  Table: bus_routes, bus_details
  Primary Key: To ensure each record is unique, an auto-incrementing primary key (id) is used.

**5. FUNCTIONALITY:**

  Red_Bus_Route_Data_Collection.ipynb
    1. used to extract the RTC bus links. Save it into a sql DataBase
    2. Uses RTC bus Links to extract bus route data - "Route Name" and "Route Link".
    3. Save the route data into a sql Data Base
  
  Red_bus_Bus_data_Extraction.ipynb
    1. Collects bus details as described in section 3.2
    2. save the bus details to sql database
  
  red_bus_streamlit.py
    1. provides user interface to select the route in a selection box
    2. the selection box is linked with the route data --> route_name
    3. Upon selection, extracts the bus details with selected route name.
    4. output in form of st.dataframe
