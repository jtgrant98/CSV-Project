import csv
from datetime import datetime


#open each CSV file
open_file1 = open("death_valley_2018_simple.csv", "r")

open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file1 = csv.reader(open_file1,delimiter=",")

csv_file2 = csv.reader(open_file2,delimiter=",")

header_row1 = next(csv_file1)

header_row2 = next(csv_file2)

print(type(header_row1))
print(type(header_row2))

for index, column_header in enumerate(header_row1):
    print(index, column_header)

for index, column_header in enumerate(header_row2):
    print(index, column_header)

#create lists
highs = []
dates = []
lows = []
highs_2 = []
dates_2 = []
lows_2 = []

#testing the datetime strptime function
#mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(mydate)
#print(type(mydate))



#allowing the exception for the loop to still run if there is no date in the column


for row in csv_file1:
    try:
        the_date = datetime.strptime(row[2],"%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
        
    except ValueError:
        print(f"Misssing data for {the_date}")
    
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)


for row in csv_file2:
    try:
        the_date = datetime.strptime(row[2],"%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        
    except ValueError:
        print(f"Misssing data for {the_date}")
    
    else:
        highs_2.append(high)
        lows_2.append(low)
        dates_2.append(the_date)
   



#testing to convert date from string
import matplotlib.pyplot as plt



#print(highs)
#print(dates)
    
fig = plt.figure()

    




#plt.plot(dates, highs, c="red", alpha=0.5)
#plt.plot(dates, lows, c="blue", alpha=0.5)




   
#fig.autofmt_xdate()



#plt.show()


#created subplots and gave specifications
plt.subplot(2,1,1)
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.title("Death Valley, CA")
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major",labelsize=12)
plt.fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()


plt.subplot(2,1,2)
plt.plot(dates_2, highs_2, c="red")
plt.plot(dates_2, lows_2, c="blue")
plt.title("Sitka Airport, AK")
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major",labelsize=12)
plt.fill_between(dates_2,highs_2,lows_2, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()


plt.suptitle("Temperature comparison between Death Valley, CA and Sitka Airport, AK", fontsize=12)

plt.show()
