# Nardos Gebremedhin
# Module 4.2
# 11/08/2024
# making changes to a program that already works
# allow the user to select whether they want to see the high temperatures or the low temperatures, or to exit
# When the user selects 'lows', they should see a graph, in blue, that reflects the lows for those dates
# Allow the program to loop until the user selects exit.
# When the user exits, provide an exit message.
# Use what elements you can from previous programs, perhaps including sys to help the exit process.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []  # added low temp to the list
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        lows.append(low)
        highs.append(high)

while True:
    # Display the menu
    print("Welcome to the Sitka Weather Program!")
    print("Use this menu to view weather data:")
    print("Please choose an option:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

    # allow the user to choose their options
    choice = input('Enter your choice (1, 2, or 3): ')

    if choice == '1':
        # Plot the high temperatures if user selects option 1
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '2':
        # Plot the low temperatures if user selects option 2
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')  # Plot lows in blue
        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

    elif choice == '3':
        # Exit the program with a goodbye message
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        exit()

    else:
        # invalid input
        print("Invalid choice. Please enter 1, 2, or 3).")
