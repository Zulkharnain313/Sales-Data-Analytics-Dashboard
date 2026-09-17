# Sales Data Analytics Dashboard

A portfolio-ready end-to-end sales analytics project using **Python, SQL and Power BI**.

## Objective
Analyze sales performance and identify trends across revenue, profit, products,
categories and regions.

## Tech Stack
- Python
- Pandas
- NumPy
- SQL / SQLite
- Power BI
- DAX
- Git/GitHub

## Project Workflow

CSV Sales Data
      ↓
Python / Pandas
      ↓
Cleaning + Feature Engineering
      ↓
SQL Database
      ↓
SQL Analysis
      ↓
Power BI
      ↓
Interactive Dashboard

## Folder Structure

```text
Sales-Data-Analytics-Dashboard/
├── data/
│   ├── sales_data.csv
│   └── cleaned_sales_data.csv
├── python/
│   ├── data_cleaning.py
│   └── data_loading.py
├── sql/
│   └── sales_analysis.sql
├── powerbi/
│   ├── DAX_Measures.txt
│   └── README_POWERBI.md
├── screenshots/
├── requirements.txt
└── README.md
```

## How to Run

### 1. Create a virtual environment (optional)

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

### 2. Install packages

```bash
pip install -r requirements.txt
```

### 3. Clean the data

```bash
python python/data_cleaning.py
```

### 4. Load into SQLite

```bash
python python/data_loading.py
```

This creates:

```text
data/sales.db
```

### 5. Run SQL analysis

Open `sql/sales_analysis.sql` in a SQLite client such as DB Browser for SQLite.

### 6. Build the Power BI dashboard

Follow `powerbi/README_POWERBI.md` and use `powerbi/DAX_Measures.txt`.

## Dashboard KPIs

- Total Sales
- Total Profit
- Total Orders
- Total Quantity
- Average Order Value
- Profit Margin

## Suggested Business Questions

1. How are sales changing month by month?
2. Which category generates the most revenue?
3. Which region has the highest revenue?
4. Which products are top sellers?
5. Which categories/products generate the most profit?
6. Are high-revenue products also highly profitable?

## Business Insights

Write conclusions only after checking the dashboard. Examples:

- Identify the strongest revenue category.
- Identify the strongest/weakest region.
- Find products with high revenue but relatively low profit margin.
- Identify months with unusually high or low sales.
- Suggest targeted actions based on observed data.

## Resume Description

**Sales Data Analytics Dashboard | Python, SQL, Power BI | Oct 2024**
- Developed an interactive Power BI dashboard to analyze sales trends, revenue, profit, product categories, and regional performance.
- Automated data cleaning and feature engineering using Python/Pandas and loaded the processed data into SQL for analytical querying.
- Created DAX measures and KPI visualizations for revenue, profit margin, order volume, and average order value.
- Generated data-driven insights by analyzing product, category, regional, and monthly sales performance.

## Important
The included CSV is synthetic portfolio data created for practice. Replace it
with a real/public dataset if you want to demonstrate external business data.
Do not claim daily automation, cloud deployment, or scheduled refresh unless
you actually configure and test it.
