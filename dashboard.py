import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Superstore Data Visualization Dashboard")
st.write("An interactive dashboard to explore sales, profit, quantity, and regional performance.")

data=pd.read_csv("dataset/superstore.csv")

#KPI numbers
total_sales = data["Sales"].sum()
total_profit = data["Profit"].sum()
total_quantity = data["Quantity"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Quantity", f"{total_quantity:,.0f}")

#Dataset
st.subheader("Dataset Preview")
st.dataframe(data.head())


#Sales by Category/Profit

col1, col2= st.columns(2)

with col1:
  st.subheader("Sales by Category")

  category_sales=data.groupby("Category")["Sales"].sum()
  st.bar_chart(category_sales)

with col2:
   st.subheader("Sales by Profit")

   category_profit=data.groupby("Category")["Profit"].sum()
   st.bar_chart(category_profit)


st.subheader("Monthly Sales")

data["Order Date"] = pd.to_datetime(data["Order Date"])

monthly_sales = data.groupby(
    data["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

st.line_chart(monthly_sales)

#sales by region
col1, col2, col3=st.columns([1,2,1])

with col2:
  st.subheader("Sales by Region")

  region_sales = data.groupby("Region")["Sales"].sum()

  st.bar_chart(region_sales, width=800)








