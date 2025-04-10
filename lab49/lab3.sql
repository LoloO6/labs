-- Step 1: Delete a user by email
DELETE FROM users
WHERE email = 'bob@example.com';

-- Step 2: Delete users older than 30
DELETE FROM users
WHERE age > 30;

-- Step 3: Verify remaining records
SELECT * FROM users;