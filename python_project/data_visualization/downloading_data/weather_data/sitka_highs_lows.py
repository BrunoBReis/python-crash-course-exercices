from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(
    'python_project/data_visualization/downloading_data/weather_data/sitka_weather_2021_simple.csv')
# Transforms this csv file in text file and split each line
lines = path.read_text().splitlines()

# Parse each line, giving an object that each line is a list
reader = csv.reader(lines)
# Get the first line
header_row = next(reader)
# print(header_row)

# enumerate returns both index and each item
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extracting date and high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# Alpha is transperancy in graph
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("Daily high and low temperatures", fontsize=24)
ax.set_xlabel('', fontsize=11)
fig.autofmt_xdate() # Format date
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)


plt.show()
