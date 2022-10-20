#Stock Data Visualizer Scrum Team 13

i = True
while i:
    # Print Title
    print("Stock Data Visualizer")
    print("-----------------------\n")

    # P1. Get Stock Symbol
    stockSymbol = input("Enter the stock symbol you are looking for: ")

    # P2. Get Chart Type
    chartType = 0
    while chartType != "1" and chartType != "2":
        print("\nChart Types")
        print("-------------")
        print("1. Bar")
        print("2. Line\n")
        chartType = input("Enter the chart type you want (1, 2): ")
        if chartType != "1" and chartType != "2": print("Enter a 1 or 2 for chart type")


    # P3. Get Time Series
    time_series = 0
    while time_series != 1 and time_series != 2 and time_series != 3 and time_series != 4:
        print("Select the Time Series of the chart you want to Generate: ")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly")
        time_series = int(input("\nEnter time series option (1, 2, 3, 4): "))
        if time_series < 0:
            print("Error: Please enter a value within the range.")
        elif time_series > 4:
            print("Error: Please enter a value within the range.")
    # P4. Get Start Date

    # P5. Get End Date

    # P6. Generate Graph
    
    # Ask to repeat
    choice = input("\nWould you like to view more stock data? Press 'y' to continue: ")
    if(choice != 'y'):
        i = False