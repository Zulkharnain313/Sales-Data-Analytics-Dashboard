"""
Sales Data Analytics Dashboard
Data cleaning and feature engineering pipeline.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"

def clean_sales_data():
    df = pd.read_csv(INPUT_FILE)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Convert data types
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    numeric_cols = ["quantity", "unit_price", "discount", "sales", "profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove duplicate orders and invalid rows
    df = df.drop_duplicates(subset=["order_id"])
    df = df.dropna(subset=["order_id", "order_date", "product", "category", "region"])
    df = df[df["quantity"] > 0]
    df = df[df["sales"] >= 0]
    df = df[df["profit"] >= 0]

    # Fill numeric missing values
    for col in numeric_cols:
        df[col] = df[col].fillna(0)

    # Feature engineering
    df["year"] = df["order_date"].dt.year
    df["month_number"] = df["order_date"].dt.month
    df["month_name"] = df["order_date"].dt.strftime("%b")
    df["quarter"] = "Q" + df["order_date"].dt.quarter.astype(str)
    df["profit_margin"] = (df["profit"] / df["sales"].replace(0, pd.NA) * 100).fillna(0).round(2)

    df = df.sort_values("order_date")
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Saved {len(df):,} cleaned rows to {OUTPUT_FILE}")

if __name__ == "__main__":
    clean_sales_data()
