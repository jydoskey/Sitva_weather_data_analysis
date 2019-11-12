import csv

#Get high temperatures from file
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #Prints all the headings 
#    print(header_row)

    #Prints a well formatted heading with its index
#    for index, column_header in enumerate(header_row):
#        print(index, column_header)

    highs = []
    for row in reader:
        #Int format of the highest temperature
        high = int(row[1])
        highs.append(high)
        
        #String format of the highest temperature
#        highs.append(row[1])
         
    
    print(highs)