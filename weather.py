# importing the library
import csv
from os import stat
import requests
from bs4 import BeautifulSoup
import numpy
from scipy import stats
import matplotlib.pyplot as plt

# set - e
# for year in $(seq 2013 2021)
# do
# curl "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=51337&Year=${year}&timeframe=2" > victoria-weather -$year.csv
# done


with open('data/victoria-weather-2020.csv') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

# enter city name
city = "orem"

# create url
url = "https://www.google.com/search?q="+"weather"+city

# requests instance
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')

# get the temperature
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

# this contains time and sky description
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# format the data
data = str.split('\n')
time = data[0]
sky = data[1]

# list having all div tags having particular clas sname
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

# particular list with required data
strd = listdiv[5].text

# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]


rainfall = weather['Total Precip (mm)'].to_list()
plt.plot(rainfall)
plt.show()
# printing all the data
# print("Temperature is", temp)
# print("Time: ", time)
# print("Sky Description: ", sky)
# print(other_data)


fig = plt.figure(figsize=(10.0, 7.0), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])

for year, annual_data in rainfall_by_year:
    days_since_jan1 = annual_data['days_since_jan1'].to_list()
    rainfall = annual_data['rainfall'].cumsum().to_list()
    ax.plot(days_since_jan1, rainfall, label=year)

# label the axes and title the plot
ax.set_xlabel('days since jan 1st')
ax.set_ylabel('precipitation (mm)')
ax.set_title('Victoria BC cumulative annual precipitation')

ax.legend()

# save the plot to disk
fig.savefig('cumulative-annual-precipitation.png', bbox_inches='tight')


def data_mean(data):
    data_mean = numpy.mean(data)
    return data_mean


def data_median(data):
    data_median = numpy.median(data)
    return data_median


def data_mode(data):
    data_mode = stats.mode(data)
    return data_mode


def stadev(data):
    stadev = numpy.std(data)
    return stadev


def trimmed_mean(data, percent):
    trimmed_mean = stats.trim_mean(data, percent)
    return trimmed_mean


def variance(data):
    # Number of observations
    n = len(data)
    # Mean of the data
    mean = sum(data) / n
    # Square deviations
    deviations = [(x - mean) ** 2 for x in data]
    # Variance
    variance = sum(deviations) / n
    return variance
