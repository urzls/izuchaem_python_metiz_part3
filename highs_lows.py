import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Чтение дат, температурных максимумов и минимумов из файла.
# filename = 'data\sitka_weather_2014.csv'
filename = 'data\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10, 6))
#plt.plot(dates, highs, c='red')
#plt.plot(dates, lows, c='blue')
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.4)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# Форматирование диаграммы.
# plt.title("Daily high and low temperatures - 2014", fontsize=14)
# plt.xlabel('Dates', fontsize=10)
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()

