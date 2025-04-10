-- Step 1: Begin a transaction
BEGIN;

-- Step 2: Insert a new record
INSERT INTO users (name, email, age) VALUES
('David Green', 'david@example.com', 40);

-- Step 3: Update an existing record
UPDATE users
SET age = 35
WHERE name = 'Alice Johnson';

-- Step 4: Delete a record
DELETE FROM users
WHERE name = 'Charlie Brown';

-- Step 5: Rollback to undo the changes
ROLLBACK;

-- Step 6: Verify that no changes were committed
SELECT * FROM users;