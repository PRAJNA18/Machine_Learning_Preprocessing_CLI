import pandas as pd
from os import path
import sys

def show_columns(data):
    print("\nColumns:\n")
    for column in data.columns.values:
        print(column, end="  ")
    print()

def print_null_values(data):
    print("\nNULL values of each column:")
    for column in data.columns.values:
        print(f'{column: <20}{sum(pd.isnull(data[column]))}')
    print()

def remove_column(data):
    show_columns(data)
    while True:
        columns = input("\nEnter all the columns you want to delete (Press -1 to go back): ").lower()
        if columns == "-1":
            break

        choice = input("Are you sure? (y/n): ").lower()
        if choice == "y":
            try:
                data.drop(columns.split(), axis=1, inplace=True)
                print("Columns removed successfully.")
            except KeyError:
                print("One or more columns are not present. Try again.")
        else:
            print("Operation cancelled.")
    return data

def fill_null_with_mean(data):
    show_columns(data)
    while True:
        column = input("\nEnter the column name (Press -1 to go back): ").lower()
        if column == "-1":
            break
        choice = input("Are you sure? (y/n): ").lower()
        if choice == "y":
            try:
                data[column] = data[column].fillna(data[column].mean())
                print("Null values filled with mean successfully.")
            except KeyError:
                print("Column is not present. Try again.")
            except TypeError:
                print("Imputation is not possible for this column. Try another column.")
        else:
            print("Operation cancelled.")
    return data

def fill_null_with_median(data):
    show_columns(data)
    while True:
        column = input("\nEnter the column name (Press -1 to go back): ").lower()
        if column == "-1":
            break
        choice = input("Are you sure? (y/n): ").lower()
        if choice == "y":
            try:
                data[column] = data[column].fillna(data[column].median())
                print("Null values filled with median successfully.")
            except KeyError:
                print("Column is not present. Try again.")
            except TypeError:
                print("Imputation is not possible for this column. Try another column.")
        else:
            print("Operation cancelled.")
    return data

def fill_null_with_mode(data):
    show_columns(data)
    while True:
        column = input("\nEnter the column name (Press -1 to go back): ").lower()
        if column == "-1":
            break
        choice = input("Are you sure? (y/n): ").lower()
        if choice == "y":
            try:
                data[column] = data[column].fillna(data[column].mode()[0])
                print("Null values filled with mode successfully.")
            except KeyError:
                print("Column is not present. Try again.")
            except TypeError:
                print("Imputation is not possible for this column. Try another column.")
        else:
            print("Operation cancelled.")
    return data

def fill_null_with_value(data):
    show_columns(data)
    while True:
        column = input("\nEnter the column name (Press -1 to go back): ").lower()
        if column == "-1":
            break
        value = input("Enter the value to fill nulls with: ")
        choice = input("Are you sure? (y/n): ").lower()
        if choice == "y":
            try:
                data[column] = data[column].fillna(value)
                print("Null values filled with specified value successfully.")
            except KeyError:
                print("Column is not present. Try again.")
        else:
            print("Operation cancelled.")
    return data

def drop_rows_with_nulls(data):
    choice = input("Are you sure you want to drop rows with any null values? (y/n): ").lower()
    if choice == "y":
        data.dropna(inplace=True)
        print("Rows with null values dropped successfully.")
    else:
        print("Operation cancelled.")
    return data

def save_dataset(data):
    filename = input("Enter the filename to save the dataset (with .csv extension): ")
    try:
        data.to_csv(filename, index=False)
        print(f"Dataset saved successfully as {filename}.")
    except Exception as e:
        print(f"Failed to save the dataset. Error: {e}")

def show_summary_statistics(data):
    print("\nSummary Statistics:")
    print(data.describe())

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

def imputer(data):
    tasks = [
        "\n1. Show number of Null Values",
        "2. Remove Columns",
        "3. Fill Null Values (with mean)",
        "4. Fill Null Values (with median)",
        "5. Fill Null Values (with mode)",
        "6. Fill Null Values (with specified value)",
        "7. Drop rows with null values",
        "8. Show the Dataset",
        "9. Save the modified dataset",
        "10. Show summary statistics"
    ]
    
    while True:
        print("\nImputation Tasks:")
        for task in tasks:
            print(task)

        try:
            choice = int(input("\nWhat do you want to do? (Press -1 to go back): "))
        except ValueError:
            print("Integer value required. Try again.")
            continue

        if choice == -1:
            break

        elif choice == 1:
            print_null_values(data)

        elif choice == 2:
            data = remove_column(data)

        elif choice == 3:
            data = fill_null_with_mean(data)

        elif choice == 4:
            data = fill_null_with_median(data)

        elif choice == 5:
            data = fill_null_with_mode(data)

        elif choice == 6:
            data = fill_null_with_value(data)

        elif choice == 7:
            data = drop_rows_with_nulls(data)

        elif choice == 8:
            show_dataset(data)

        elif choice == 9:
            save_dataset(data)

        elif choice == 10:
            show_summary_statistics(data)

        else:
            print("Invalid choice. Please try again.")

    return data

