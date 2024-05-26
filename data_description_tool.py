import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_dataset(data):
    while True:
        try:
            rows = int(input("\nHow many rows (>0) to print? (Press -1 to go back): "))
            if rows == -1:
                break
            if rows <= 0:
                print("Number of rows must be positive.")
                continue
            print(data.head(rows))
        except ValueError:
            print("Numeric value is required. Please try again.")

def describe_specific_column(data):
    show_columns(data)
    while True:
        column_name = input("\nWhich column would you like to describe? (Press Enter to go back): ").lower()
        if column_name == "":
            break
        try:
            print(data[column_name].describe())
            while True:
                visualize = input("\nWould you like to visualize this column? (yes/no): ").lower()
                if visualize == "yes":
                    sns.histplot(data[column_name])
                    plt.title(f"Distribution of {column_name}")
                    plt.xlabel(column_name)
                    plt.show()
                    break
                elif visualize == "no":
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        except KeyError:
            print("No column with this name. Please try again.")

def show_columns(data):
    print("\nColumns:")
    for column in data.columns:
        print(column, end="  ")

def show_properties(data):
    print("\nDataset Properties:")
    print(data.describe())
    print("\nDataset Information:")
    print(data.info())

def handle_outliers(data):
    while True:
        column_name = input("\nWhich column would you like to handle outliers for? (Press Enter to go back): ").lower()
        if column_name == "":
            break
        try:
            q1 = data[column_name].quantile(0.25)
            q3 = data[column_name].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            outliers = data[(data[column_name] < lower_bound) | (data[column_name] > upper_bound)]
            if not outliers.empty:
                print("\nOutliers:")
                print(outliers)
                action = input("\nWould you like to remove outliers? (yes/no): ").lower()
                if action == "yes":
                    data = data[(data[column_name] >= lower_bound) & (data[column_name] <= upper_bound)]
                    print("Outliers removed.")
        except KeyError:
            print("No column with this name. Please try again.")

def summary_statistics(data):
    show_columns(data)
    while True:
        column_name = input("\nFor which column do you want summary statistics? (Press Enter to go back): ").lower()
        if column_name == "":
            break
        try:
            print("\nSummary Statistics:")
            print(data[column_name].describe())
        except KeyError:
            print("No column with this name. Please try again.")

def describe_dataset(data):
    while True:
        print("\nTasks (Data Description):\n")
        print("1. Describe a specific column")
        print("2. Show properties of the dataset")
        print("3. Show the dataset")
        print("4. Handle outliers")
        print("5. Summary statistics for a specific column")
        print("-1. Go back")

        while True:
            try:
                choice = int(input("\nWhat would you like to do? "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            break

        if choice == -1:
            break

        elif choice == 1:
            describe_specific_column(data)

        elif choice == 2:
            show_properties(data)

        elif choice == 3:
            show_dataset(data)

        elif choice == 4:
            handle_outliers(data)

        elif choice == 5:
            summary_statistics(data)

        else:
            print("Invalid choice. Please try again.")
