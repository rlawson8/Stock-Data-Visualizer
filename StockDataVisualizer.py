#P6

if chartType == 1:
    bar_chart = pygal.Bar()
    bar_chart.title = 'Stock Data for ' + stockSymbol + ': ' + startDate + ' to ' + endDate
    if timeSeries == 1:
        bar_chart.x_labels = startDate.day
    elif timeSeries == 2:
        bar_chart.x_labels = map(str, range(startDate.day, endDate.day))
    elif timeSeries == 3:
        bar_chart.x_labels = map(str, range(startDate.day, endDate.day, 7))
    else:
        bar_chart.x_labels = map(str, range(startDate.month, endDate.month))
    bar_chart.add('Open', [])
    bar_chart.add('High',  [])
    bar_chart.add('Low',      [])
    bar_chart.add('Close',  [])
    bar_chart.render()

line_chart = pygal.Line()
line_chart.title = 'Stock Data for ' + stockSymbol + ': ' + startDate + ' to ' + endDate
if timeSeries == 1:
        bar_chart.x_labels = startDate.day
    elif timeSeries == 2:
        bar_chart.x_labels = map(str, range(startDate.day, endDate.day))
    elif timeSeries == 3:
        bar_chart.x_labels = map(str, range(startDate.day, endDate.day, 7))
    else:
        bar_chart.x_labels = map(str, range(startDate.month, endDate.month))
line_chart.add('Open', [])
line_chart.add('High',  [])
line_chart.add('Low',      [])
line_chart.add('Close',  [])
line_chart.render()
