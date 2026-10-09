SELECT 
    customers.name,
    orders.order_date
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;

SELECT 
    c.*
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;

SELECT 
    c.customer_id,
    c.name,
    COUNT(o.customer_id) AS orders_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY orders_count DESC
LIMIT 3;

SELECT 
    c.name,
    COUNT(o.customer_id) AS orders_count
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.customer_id) > 2;

SELECT *
FROM orders
WHERE order_date >= '2023-12-01' 
  AND order_date < '2024-01-01';

SELECT 
    o.*
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.name ILIKE '%Алексей%';

SELECT *
FROM products 
WHERE stock_quantity = 0 OR stock_quantity = NULL;

