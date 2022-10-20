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
