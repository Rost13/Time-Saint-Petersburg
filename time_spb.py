# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from datetime import datetime
from pytz import timezone

# Set timezone to 'Europe/Moscow'
tz = timezone('Europe/Moscow')

# Get current time in the timezone
current_time = datetime.now(tz)

# Format the time to remove the date
time_only = current_time.strftime("%H:%M:%S")

print(time_only)