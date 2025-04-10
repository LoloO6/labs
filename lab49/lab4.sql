-- Step 1: Create the 'products' table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL,
    discontinued BOOLEAN DEFAULT FALSE
);

-- Step 2: Insert products into the table
INSERT INTO products (product_name, price, stock_quantity) VALUES
('Laptop', 999.99, 10),
('Smartphone', 599.99, 20),
('Headphones', 199.99, 15);

-- Step 3: Update the price of a product
UPDATE products
SET price = 1099.99
WHERE product_name = 'Laptop';

-- Step 4: Mark a product as discontinued
UPDATE products
SET discontinued = TRUE
WHERE product_name = 'Headphones';

-- Step 5: Delete discontinued products
DELETE FROM products
WHERE discontinued = TRUE;

-- Step 6: Verify the remaining records
SELECT * FROM products;