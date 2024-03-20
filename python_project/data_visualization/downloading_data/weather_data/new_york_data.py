from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(
    'python_project/data_visualization/downloading_data/weather_data/3635476.csv')

# Csv to file text
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Shows what each column does
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Creating a list for each list
dates, snows, prepts = [], [], []
for row in reader:
    # Get each data
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:

        prep = float(row[5])
        snow = float(row[6])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        # Appending
        # Get maximum ammount of snow and prep in each date
        if date in dates:
            if prep < prepts[-1]:
                continue
            else:
                prepts.pop()
                prepts.append(prep)
            if snow < snows[-1]:
                continue
            else:
                snows.pop()
                snows.append(snow)
            continue
        else:
            dates.append(date)  
            prepts.append(round(prep, 2))
            snows.append(snow)


# Ploting 
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.bar(dates, prepts, color='red')
ax.bar(dates, snows, color='blue', alpha=0.5)

ax.set_title("Precipitation and snow in NY")
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()