import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

def print_tasks(tasks):
    for task in tasks:
        print(task)

def show_dataset(data):
    rows = int(input("\nHow many rows(>0) to print? (Press -1 to go back): "))
    if rows == -1:
        return
    if rows > 0:
        print(data.head(rows))
    else:
        print("Number of rows given must be positive.")

def perform_normalization(data, columns=None):
    scaler = MinMaxScaler()
    if columns:
        for column in columns:
            try:
                data[column] = scaler.fit_transform(data[[column]])
            except KeyError:
                print(f"Column {column} not found.")
    else:
        data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    return data

def perform_standardization(data, columns=None):
    scaler = StandardScaler()
    if columns:
        for column in columns:
            try:
                data[column] = scaler.fit_transform(data[[column]])
            except KeyError:
                print(f"Column {column} not found.")
    else:
        data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    return data

def perform_robust_scaling(data, columns=None):
    scaler = RobustScaler()
    if columns:
        for column in columns:
            try:
                data[column] = scaler.fit_transform(data[[column]])
            except KeyError:
                print(f"Column {column} not found.")
    else:
        data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    return data

def handle_normalization(data):
    tasks_normalization = [
        "\n1. Normalize a specific column",
        "2. Normalize the entire dataset",
        "3. Show the dataset"
    ]
    while True:
        print("\nTasks (Normalization)")
        print_tasks(tasks_normalization)
        try:
            choice = int(input("\nWhat would you like to do? (Press -1 to go back): "))
        except ValueError:
            print("Integer value required. Try again.")
            continue

        if choice == -1:
            break
        elif choice == 1:
            columns = input("Enter column(s) to normalize (separate by space, Press -1 to go back): ").lower().split()
            if '-1' in columns:
                break
            data = perform_normalization(data, columns)
            print("Normalization done.")
        elif choice == 2:
            data = perform_normalization(data)
            print("Normalization done for the entire dataset.")
        elif choice == 3:
            show_dataset(data)
        else:
            print("Invalid choice. Try again.")
    return data

def handle_standardization(data):
    tasks_standardization = [
        "\n1. Standardize a specific column",
        "2. Standardize the entire dataset",
        "3. Show the dataset"
    ]
    while True:
        print("\nTasks (Standardization)")
        print_tasks(tasks_standardization)
        try:
            choice = int(input("\nWhat would you like to do? (Press -1 to go back): "))
        except ValueError:
            print("Integer value required. Try again.")
            continue

        if choice == -1:
            break
        elif choice == 1:
            columns = input("Enter column(s) to standardize (separate by space, Press -1 to go back): ").lower().split()
            if '-1' in columns:
                break
            data = perform_standardization(data, columns)
            print("Standardization done.")
        elif choice == 2:
            data = perform_standardization(data)
            print("Standardization done for the entire dataset.")
        elif choice == 3:
            show_dataset(data)
        else:
            print("Invalid choice. Try again.")
    return data

def handle_robust_scaling(data):
    tasks_robust_scaling = [
        "\n1. Apply Robust Scaling to a specific column",
        "2. Apply Robust Scaling to the entire dataset",
        "3. Show the dataset"
    ]
    while True:
        print("\nTasks (Robust Scaling)")
        print_tasks(tasks_robust_scaling)
        try:
            choice = int(input("\nWhat would you like to do? (Press -1 to go back): "))
        except ValueError:
            print("Integer value required. Try again.")
            continue

        if choice == -1:
            break
        elif choice == 1:
            columns = input("Enter column(s) to robust scale (separate by space, Press -1 to go back): ").lower().split()
            if '-1' in columns:
                break
            data = perform_robust_scaling(data, columns)
            print("Robust scaling done.")
        elif choice == 2:
            data = perform_robust_scaling(data)
            print("Robust scaling done for the entire dataset.")
        elif choice == 3:
            show_dataset(data)
        else:
            print("Invalid choice. Try again.")
    return data

def feature_scaling(data):
    tasks = [
        "\n1. Perform Normalization (MinMax Scaler)",
        "2. Perform Standardization (Standard Scaler)",
        "3. Perform Robust Scaling (Robust Scaler)",
        "4. Show the Dataset"
    ]
    while True:
        print("\nFeature Scaling Tasks")
        print_tasks(tasks)
        try:
            choice = int(input("\nWhat would you like to do? (Press -1 to go back): "))
        except ValueError:
            print("Integer value required. Try again.")
            continue

        if choice == -1:
            break
        elif choice == 1:
            data = handle_normalization(data)
        elif choice == 2:
            data = handle_standardization(data)
        elif choice == 3:
            data = handle_robust_scaling(data)
        elif choice == 4:
            show_dataset(data)
        else:
            print("Invalid choice. Try again.")
    return data

