import streamlit as st
import pandas as pd
from utils.cleaning import clean_data
from utils.kpis import calculate_kpis
from utils.charts import (
    plot_sales_trend,
    plot_top_products,
    plot_category_pie,
    plot_sales_heatmap,
)


st.set_page_config(page_title="Business Insights Dashboard", layout="wide")
st.title("📊 Business Data Insights Dashboard")


uploaded_file = st.file_uploader("Upload your CSV data", type=["csv"])


if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())


    df = clean_data(df)


    st.subheader("Cleaned Data Preview")
    st.dataframe(df.head())


    # Date Range Filter
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        min_date = df["date"].min()
        max_date = df["date"].max()


    date_range = st.date_input("Select Date Range", [min_date, max_date])


    if len(date_range) == 2:
        start, end = date_range
        df = df[(df["date"] >= pd.to_datetime(start)) & (df["date"] <= pd.to_datetime(end))]


    # KPIs
    kpis = calculate_kpis(df)


    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)


    col1.metric("Total Revenue", f"${kpis['total_revenue']:,}")
    col2.metric("Top Product", kpis["top_product"])
    col3.metric("Total Transactions", kpis["total_transactions"])


    # Charts
    st.subheader("Sales Trend")
    st.plotly_chart(plot_sales_trend(df), use_container_width=True)


    st.subheader("Top Products")
    st.plotly_chart(plot_top_products(df), use_container_width=True)


    st.subheader("Sales by Category")
    st.plotly_chart(plot_category_pie(df), use_container_width=True)


    st.subheader("Sales Heatmap")
    st.plotly_chart(plot_sales_heatmap(df), use_container_width=True)
