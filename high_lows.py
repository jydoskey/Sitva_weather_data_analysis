import csv

from datetime import datetime
from matplotlib import pyplot as plt

#Get high temperatures from file
filename = 'sitka_weather_07-2014.csv'
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
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        #-3a- Int format of the highest temperature
        high = int(row[1])
        highs.append(high)
        
        #-3b- String format of the highest temperature
#       highs.append(row[1])
        
# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
            
#    print(highs)