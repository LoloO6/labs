import time
from datetime import datetime, timedelta

#1
now = datetime.now() #get current time and date

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_now)

#2
from datetime import datetime

# Get the current date and time
today = datetime.now()

# Define a future event date (New Year's Eve)
new_years_eve = datetime(today.year, 12, 31)

# If today is already New Year's Eve or later in the year, adjust for the next year
if today > new_years_eve:
    new_years_eve = datetime(today.year + 1, 12, 31)

# Calculate the difference between the two dates
time_until_new_year = new_years_eve - today

# Print the number of days until New Year's Eve
print("Days until New Year's Eve:", time_until_new_year.days)

#3

def countdown_timer(seconds):
    # Calculate the end time by adding a timedelta to the current time
    end_time = datetime.now() + timedelta(seconds=seconds)

    while True:
        # Calculate the remaining time
        remaining = end_time - datetime.now()
        total_seconds = int(remaining.total_seconds())

        if total_seconds <= 0:
            print("Time remaining: 0 seconds")
            break

        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")

# Start a 10-second timer
countdown_timer(10)

#4

def simple_month_calendar(year, month):
    # Start with the first day of the month
    current_date = datetime(year, month, 1)

    # Determine the weekday for the first day (Monday = 0, Sunday = 6)
    start_weekday = current_date.weekday()

    # Determine the last day of the month
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)

    last_date = next_month - timedelta(days=1)

    # Print the calendar header
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Print indentation for the first week
    print("    " * start_weekday, end="")

    # Loop through all the days of the month
    while current_date <= last_date:
        print(f"{current_date.day:3}", end=" ")
        if current_date.weekday() == 6:  # Start a new line on Sunday
            print()
        current_date += timedelta(days=1)

    print()  # New line at the end


# Generate a calendar for May 2025
simple_month_calendar(2025, 5)


