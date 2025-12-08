import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(how="all") # Remove empty rows
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]

    # Convert numeric columns
    for col in df.columns:
        if col in ["sales", "revenue", "amount", "price"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df