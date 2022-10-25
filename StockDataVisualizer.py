#P6

import pygal
import datetime
import requests

format = "%Y-%m-%d"
startDate_dt = datetime.datetime.strptime(startDate, format)
endDate_dt = datetime.datetime.strptime(endDate, format)
dateKeyList = []
openValues = []
highValues = []
lowValues = []
closeValues = []

if chartType == 1:
    chart = pygal.Bar()
else:
    chart = pygal.Line()
chart.title = 'Stock Data for ' + stockSymbol + ': ' + startDate + ' to ' + endDate
if timeSeries == 1:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+stockSymbol+'&interval=60min&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
elif timeSeries == 2:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+stockSymbol+'&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
elif timeSeries == 3:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+stockSymbol+'&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
else:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+stockSymbol+'&outputsize=full&apikey=TF2MH4AQ3EMH4GZL'
r = requests.get(url)
data = r.json()
data.pop('Meta Data')
dateList = data.values()
for dictionary in dateList:
    for dateKey in dictionary:
        dateKey_dt = datetime.datetime.strptime(dateKey, format)
        if dateKey_dt.day in range(startDate_dt.day, endDate_dt.day+1) and dateKey_dt.month in range(startDate_dt.month, endDate_dt.month+1) and dateKey_dt.year in range(startDate_dt.year, endDate_dt.year+1):
            dateKeyList.append(dateKey)
            openValues.append(float(dictionary[dateKey]['1. open']))
            highValues.append(float(dictionary[dateKey]['2. high']))
            lowValues.append(float(dictionary[dateKey]['3. low']))
            closeValues.append(float(dictionary[dateKey]['4. close']))
dateKeyList.reverse()
openValues.reverse()
highValues.reverse()
lowValues.reverse()
closeValues.reverse()
chart.x_labels = map(str, dateKeyList)
chart.add('Open', openValues)
chart.add('High',  highValues)
chart.add('Low',      lowValues)
chart.add('Close',  closeValues)
chart.render_in_browser()
