# Practical 10 - Date Handling - Execution Time Measurement & Calendar Operations

from datetime import datetime, date
import time
import calendar

# Date Handling

print("DATE HANDLING")

today = date.today()
# Returns the current system date.
# Example Output: 2026-06-21

print("Today's Date:", today)

now = datetime.now()
# Returns the current date and time.
# Example Output: 2026-06-21 14:30:45.123456

print("Current Date & Time:", now)

print("Formatted Date:",
      now.strftime("%d-%m-%Y %H:%M:%S"))
# strftime() formats the date and time according to the given pattern.
# %d → Day
# %m → Month
# %Y → Year
# %H → Hour (24-hour format)
# %M → Minutes
# %S → Seconds
# Example Output: 21-06-2026 14:30:45

# Execution Time Measurement

print("\nEXECUTION TIME")

start = time.perf_counter()
# Records the starting time with high precision.

for i in range(1000000):
    pass
# Executes an empty loop 1,000,000 times.

end = time.perf_counter()
# Records the ending time.

print("Execution Time:",
      end - start,
      "seconds")
# Calculates and displays the time taken by the loop.
# Output depends on system performance.

# Calendar Operations

print("\nCALENDAR")

print(calendar.month(2026, 6))
# Displays the calendar for June 2026.

print("Leap Year 2024:",
      calendar.isleap(2024))
# Checks whether 2024 is a leap year.
# Output: True

print("Weekday Number:",
      calendar.weekday(2026, 6, 20))
# Returns weekday number for a given date.
# Monday = 0
# Tuesday = 1
# Wednesday = 2
# Thursday = 3
# Friday = 4
# Saturday = 5
# Sunday = 6
# Output: 5 (Saturday)