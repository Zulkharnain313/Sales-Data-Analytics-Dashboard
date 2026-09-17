"""
Load cleaned sales data into a SQL database.

Default: SQLite (zero configuration).
For MySQL/PostgreSQL, replace the connection string and install the
appropriate SQLAlchemy driver.
"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"
DB_FILE = BASE_DIR / "data" / "sales.db"

def load_to_sqlite():
    df = pd.read_csv(INPUT_FILE)
    engine = create_engine(f"sqlite:///{DB_FILE}")
    df.to_sql("sales", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df):,} rows into {DB_FILE}")

if __name__ == "__main__":
    load_to_sqlite()
