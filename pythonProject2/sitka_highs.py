import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        high = int(row[4])
        low = int(row[5])
        date = datetime.strptime(row[2], '%Y-%m-%d')

        highs.append(high)
        dates.append(date)
        lows.append(low)


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


plt.title('Daily high and low temperatures - 2021', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()