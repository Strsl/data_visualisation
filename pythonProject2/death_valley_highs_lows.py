import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = 'death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f'Missing data for {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(lows)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

plt.title('Daily high and low temperatures - 2021\nDeath Valley, CA')
plt.xlabel('', fontsize=20)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()