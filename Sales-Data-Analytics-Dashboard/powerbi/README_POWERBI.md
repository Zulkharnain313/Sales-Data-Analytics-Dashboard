# Power BI Dashboard Build Guide

## Import
1. Open Power BI Desktop.
2. Get Data -> Text/CSV -> `data/cleaned_sales_data.csv`.
3. Set `order_date` to Date.
4. Set `sales`, `profit`, and `unit_price` to Decimal Number.
5. Set `quantity` to Whole Number.
6. Create the DAX measures in `DAX_Measures.txt`.

## Recommended dashboard
- KPI Cards: Total Sales, Total Profit, Total Orders, Profit Margin %
- Line chart: Sales by Month
- Column chart: Revenue by Category
- Bar chart: Revenue by Region
- Bar chart: Top 10 Products by Revenue
- Column chart: Profit by Category
- Slicers: Year, Region, Category, Product

## Data model
For a beginner project, the cleaned Sales table is sufficient.
For an advanced version, create a separate Date table and use a star schema.

## Refresh
For a local portfolio project, refresh the dataset after running the Python
pipeline. For a cloud deployment, configure scheduled refresh using a
supported gateway/data source setup.
