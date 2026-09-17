-- Sales Data Analytics Dashboard
-- SQL analysis queries (SQLite-compatible)

-- 1. Total revenue
SELECT ROUND(SUM(sales), 2) AS total_revenue
FROM sales;

-- 2. Total profit
SELECT ROUND(SUM(profit), 2) AS total_profit
FROM sales;

-- 3. Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- 4. Total quantity sold
SELECT SUM(quantity) AS total_quantity
FROM sales;

-- 5. Revenue by category
SELECT category, ROUND(SUM(sales), 2) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 6. Profit by category
SELECT category, ROUND(SUM(profit), 2) AS profit
FROM sales
GROUP BY category
ORDER BY profit DESC;

-- 7. Revenue by region
SELECT region, ROUND(SUM(sales), 2) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;

-- 8. Monthly revenue
SELECT year, month_number, month_name,
       ROUND(SUM(sales), 2) AS revenue
FROM sales
GROUP BY year, month_number, month_name
ORDER BY year, month_number;

-- 9. Top 10 products
SELECT product, ROUND(SUM(sales), 2) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 10;

-- 10. Product profitability
SELECT product,
       ROUND(SUM(sales), 2) AS revenue,
       ROUND(SUM(profit), 2) AS profit,
       ROUND(SUM(profit) / NULLIF(SUM(sales), 0) * 100, 2) AS profit_margin
FROM sales
GROUP BY product
ORDER BY profit DESC;

-- 11. Regional category performance
SELECT region, category,
       ROUND(SUM(sales), 2) AS revenue,
       ROUND(SUM(profit), 2) AS profit
FROM sales
GROUP BY region, category
ORDER BY region, revenue DESC;
