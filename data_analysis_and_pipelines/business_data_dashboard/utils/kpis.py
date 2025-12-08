import pandas as pd


def calculate_kpis(df: pd.DataFrame) -> dict:
    """calculate kpis"""
    kpis = {}

    if "revenue" in df.columns:
        kpis["total_revenue"] = df["revenue"].sum()
    else:
        kpis["total_revenue"] = 0

    if "product" in df.columns:
        kpis["top_product"] = df["product"].value_counts().idxmax()
    else:
        kpis["top_product"] = "N/A"

    kpis["total_transactions"] = len(df)

    return kpis
