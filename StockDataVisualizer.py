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

    # P4. Get Start Date

    # P5. Get End Date

    # P6. Generate Graph

    # Ask to repeat
    choice = input("\nWould you like to view more stock data? Press 'y' to continue: ")
    if(choice != 'y'):
        i = False