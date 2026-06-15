import streamlit as st
import pandas as pd
import duckdb

import sys
import subprocess

try:
    from streamlit_option_menu import option_menu
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit-option-menu"])
    from streamlit_option_menu import option_menu

conn = duckdb.connect(database=":memory:")

conn.execute("INSTALL spatial;")
conn.execute("LOAD spatial;")

st.title("Welcome to My Miniproject 2.")
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Queries"], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    
if selected == "Home":
    st.header('Ola Ride Insights.')
    st.write("The rise of OLA rides in India has transformed urban mobility, offering convenience and affordability to millions of users. OLA, a leading ride-hailing service, generates vast amounts of data related to ride bookings, driver availability, fare calculations, and customer preferences. However, deriving actionable insights from the ola dataset provided remains a challenge. To enhance operational efficiency, improve customer satisfaction, and optimize business strategies, in this project I have cleaned and analysed the OLA excel file dataset provided and created a streamlit application and a PowerBI dashboard for the data analysis and visualisation in an interactive and user-friendly manner. My goal in this project is to extract meaningful insights that can drive data-informed decisions, in this project I have extracted 10 meaningful insights from the ola excel dataset which are my key findings.")
    st.image("ola picture.jpg", caption="Jessica Sriramula")

if selected == "Queries":
    st.subheader("Analysis of all the 10 Query Data Outputs.")
    one = st.selectbox("Here 10 queries are displayed, please choose the query you want to display:", ["Query 1: All successfull bookings", 
                                                                        "Query 2: Average ride distance for each vehicle type", 
                                                                        "Query 3: Total number of cancelled rides by customers", 
                                                                        "Query 4: Top 5 customers who booked the highest number of rides", 
                                                                        "Query 5: Number of rides cancelled by drivers due to personal and car-related issues",
                                                                        "Query 6: Maximum and minimum driver ratings for Prime Sedan bookings",
                                                                        "Query 7: All rides where payment was made using UPI",
                                                                        "Query 8: Average customer rating per vehicle type", 
                                                                        "Query 9: The total booking value of rides completed successfully",
                                                                        "Query 10: All incomplete rides along with the reason"])

    if one == "Query 1: All successfull bookings":
        st.write("Here we can see all the successfull bookings for each customer.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT * FROM df WHERE Booking_Status = 'Success';"

        df_successfull_bookings = conn.execute(sql_query).df()

        st.dataframe(df_successfull_bookings)

        st.subheader("Successfull bookings vs. Vehicle Type")

        st.bar_chart(df_successfull_bookings, x="Vehicle_Type", y="Booking_Status")



    if one == "Query 2: Average ride distance for each vehicle type":
        st.write("Here we can see the average ride distance for each vehicle type.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT Vehicle_Type, AVG(Ride_Distance) AS Average_Distance FROM df GROUP BY Vehicle_Type ORDER BY Average_Distance DESC;"

        df_ride_distance = conn.execute(sql_query).df()

        st.dataframe(df_ride_distance)

        st.subheader("Average Ride Distance vs. Vehicle Type")
        
        st.bar_chart(df_ride_distance, x="Vehicle_Type", y="Average_Distance")


    if one == "Query 3: Total number of cancelled rides by customers":
        st.write("Here we can see the total number of cancelled rides by each customer which is a total of 10499.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT COUNT(*) AS Total_Customer_Cancellations FROM df WHERE Booking_Status = 'Canceled by Customer';"

        df_cancelled_rides =  conn.execute(sql_query).df()

        st.dataframe(df_cancelled_rides)


    if one == "Query 4: Top 5 customers who booked the highest number of rides":
        st.write("Here we can see the top 5 customers who booked the highest number of rides.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT Customer_ID,  COUNT(*) AS Total_Bookings FROM df GROUP BY Customer_ID ORDER BY Total_Bookings DESC LIMIT 5;"

        df_highest_rides =  conn.execute(sql_query).df()

        st.dataframe(df_highest_rides)

        st.subheader("Customer ID vs. Total Bookings")

        st.bar_chart(df_highest_rides, x="Customer_ID", y="Total_Bookings")


    if one == "Query 5: Number of rides cancelled by drivers due to personal and car-related issues":
        st.write("Here we can see the number of rides cancelled by drivers due to personal and car-related issues.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT COUNT(*) AS Driver_Issue_Cancellations FROM df WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue'";

        df_rides_cancelled =  conn.execute(sql_query).df()

        st.dataframe(df_rides_cancelled)

    
    if one == "Query 6: Maximum and minimum driver ratings for Prime Sedan bookings":
        st.write("Here we can see the maximum and minimum driver ratings for the Prime Sedan car bookings.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT MAX(Driver_Ratings) AS Maximum_Rating, MIN(Driver_Ratings) AS Minimum_Rating FROM df WHERE Vehicle_Type = 'Prime Sedan'";

        df_driver_ratings =  conn.execute(sql_query).df()

        st.dataframe(df_driver_ratings)

    
    if one == "Query 7: All rides where payment was made using UPI":
        st.write("Here we can see all the rides where the payment made by the customer was UPI.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT * FROM df WHERE Payment_Method = 'UPI'";

        df_upi_rides =  conn.execute(sql_query).df()

        st.dataframe(df_upi_rides)

        st.subheader("Vehicle Type vs. Payment Method")

        st.bar_chart(df_upi_rides, x="Vehicle_Type", y="Payment_Method")
 
    
    if one == "Query 8: Average customer rating per vehicle type":
        st.write("Here we can see all the average customer ratings for each vehicle type.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT Vehicle_Type,  ROUND(AVG(Customer_Rating), 2) AS Average_Customer_Rating FROM df WHERE Customer_Rating IS NOT NULL GROUP BY Vehicle_Type ORDER BY Average_Customer_Rating DESC";

        df_avg_customer_rating = conn.execute(sql_query).df()

        st.dataframe(df_avg_customer_rating)

        st.subheader("Average Customer Rating vs. Vehicle Type")

        st.bar_chart(df, x="Vehicle_Type", y="Average_Customer_Rating")


    if one == "Query 9: The total booking value of rides completed successfully":
        st.write("Here we can see the total booking value of the rides that were completed successfully.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT  SUM(Booking_Value) AS Total_Successful_Revenue FROM df WHERE Booking_Status = 'Success'";

        df_total_booking_value =  conn.execute(sql_query).df()

        st.dataframe(df_total_booking_value)
    

    if one == "Query 10: All incomplete rides along with the reason":
        st.write("Here we can see all the incomplete rides along with the specific reasons.")

        excel_file = r"C:/Users/pc/Desktop/miniproject2/OLA_dataset.xlsx"

        df = pd.read_excel(excel_file)

        sql_query ="SELECT Booking_ID,  Incomplete_Rides, Incomplete_Rides_Reason FROM df WHERE Incomplete_Rides = 'Yes' OR Incomplete_Rides_Reason IS NOT NULL";

        df_incomplete_rides =  conn.execute(sql_query).df()

        st.dataframe(df_incomplete_rides)

        st.subheader("Incomplete Rides Reason vs. Incomplete Rides")

        st.bar_chart(df_incomplete_rides, x="Incomplete_Rides_Reason", y="Incomplete_Rides")


