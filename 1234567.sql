select name, email
from customers 
where phone is Null;

select name
from customers 
where email LIKE '%mail.ru';

select sum(price * stock_quantity) as total
from products;

select order_id 
from orders
where status = 'pending' or status = 'shipped';

SELECT 
    orders.order_id,
    orders.order_date,
    SUM(order_items.quantity * order_items.price_per_unit) AS total_sum
FROM orders
JOIN order_items ON orders.order_id = order_items.order_id
GROUP BY orders.order_id, orders.order_date;

SELECT 
    customers.name,
    SUM(order_items.quantity * order_items.price_per_unit) AS total_spent
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN order_items ON orders.order_id = order_items.order_id
WHERE orders.status = 'delivered'
GROUP BY customers.customer_id, customers.name
ORDER BY total_spent DESC
LIMIT 1;

SELECT 
    products.name,
    SUM(order_items.quantity) AS total_units_sold
FROM products
JOIN order_items ON products.product_id = order_items.product_id
GROUP BY products.product_id, products.name
ORDER BY total_units_sold DESC
LIMIT 1;

SELECT name 
FROM products
WHERE product_id NOT IN (
    SELECT product_id 
    FROM order_items
);
