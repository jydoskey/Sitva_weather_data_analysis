import csv

from datetime import datetime
from matplotlib import pyplot as plt

#Get dates, high and low temperatures from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # -1- Prints all the headings 
#    print(header_row)

    # -2- Prints a well formatted heading with its index
#    for index, column_header in enumerate(header_row):
#        print(index, column_header)

#    -3-
    #Get dates and high temperature from file
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
        #-3a- Int format of the highest temperature
            highs.append(high)
            lows.append(low)
        
        #-3b- String format of the highest temperature
#       highs.append(row[1])
        
# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()            
#    print(highs)