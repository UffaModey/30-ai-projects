""" DOCSTRING """
import plotly.express as px
import pandas as pd


# 1. Sales Trend
def plot_sales_trend(df: pd.DataFrame):
    """plot sales trend"""
    if "date" not in df.columns or "revenue" not in df.columns:
        return px.line(title="Sales Trend (No valid date or revenue data)")

    df_sorted = df.sort_values("date")
    return px.line(df_sorted, x="date", y="revenue", title="Sales Over Time")


# 2. Top Products
def plot_top_products(df: pd.DataFrame):
    """plot top products"""
    if "product" not in df.columns or "revenue" not in df.columns:
        return px.bar(title="Top Products (Missing product or revenue column)")

    grouped = (
        df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10)
    )
    return px.bar(grouped, x=grouped.index, y=grouped.values, title="Top 10 Products")


# 3. Category Pie Chart
def plot_category_pie(df: pd.DataFrame):
    """plot category pie"""
    if "category" not in df.columns or "revenue" not in df.columns:
        return px.pie(title="Category Breakdown (Missing category or revenue column)")

    grouped = df.groupby("category")["revenue"].sum()
    return px.pie(
        names=grouped.index, values=grouped.values, title="Revenue by Category"
    )


# 4. Heatmap: Sales by Day & Hour
def plot_sales_heatmap(df: pd.DataFrame):
    """plot sales heatmap"""
    if "date" not in df.columns or "revenue" not in df.columns:
        return px.imshow([[0]], title="Heatmap Unavailable")

    df["day"] = df["date"].dt.day_name()
    df["hour"] = df["date"].dt.hour

    pivot = df.pivot_table(
        values="revenue", index="day", columns="hour", aggfunc="sum"
    ).fillna(0)

    return px.imshow(pivot, title="Sales Heatmap: Day vs Hour")
