import streamlit as st
import pandas as pd
import os
import csv

#Funtion for adding data to csv file:TrackerData
def addData(header,row):
    if os.path.exists("TrackerData.csv"):
        with open("TrackerData.csv",mode="a",newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(row)
    else:
        with open("TrackerData.csv",mode="w",newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)





st.title("Expense :blue[Tracker]")
st.subheader("Input")

#Inputting Data
col1,col2 = st.columns(2)
with col1:
    exp_name = st.text_input("Category",placeholder="Food,Travel....")
    exp_date = st.date_input("Date")
with col2:
    exp_amt = st.number_input("Amount",placeholder=200)

b1 = st.button("Submit",use_container_width=True)
if b1:
    row = [exp_name,exp_amt,exp_date]
    header = ["Category","Amount","Date"]
    addData(header,row)
    st.text("Expense Updated")

#Table View Of Data
df = pd.read_csv("TrackerData.csv")
df.index = df.index+1
st.subheader("Analysis")
uni_cat=["Normal","Total","Date"]
uni_cat = uni_cat + (df["Category"].unique()).tolist()
cat_pill = st.pills("Filter",uni_cat,default="Total",selection_mode="single")
if cat_pill is "Total":
    cat_table = df.groupby("Category")["Amount"].sum()
    st.table(cat_table)
elif cat_pill is "Date":
    cat_table = df.groupby("Date")["Amount"].sum()
    st.table(cat_table)
elif cat_pill=="Normal":
    st.table(df)
else:
    st.table(df.loc[df["Category"]==cat_pill])

tot_exp = df["Amount"].sum()
st.metric(":blue[Total Spending]",tot_exp,border=True)

#Visualizing Data
st.subheader(" Spending Trends ")
uni_chart = ["Total","Date"]
chart_pill = st.pills("Filter",uni_chart,selection_mode="single",default="Total")
if chart_pill is "Total":
    chart_table = df.groupby("Category")["Amount"].sum()
    st.bar_chart(chart_table)
if chart_pill is "Date":
    chart_table = df.groupby("Date")["Amount"].sum()
    st.bar_chart(chart_table)

