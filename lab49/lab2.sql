-- Step 1: Update the age of a user
UPDATE users
SET age = 29
WHERE name = 'Alice Johnson';

-- Step 2: Change the email of a user
UPDATE users
SET email = 'charlie.brown@example.com'
WHERE name = 'Charlie Brown';

-- Step 3: Verify the updated records
SELECT * FROM users;