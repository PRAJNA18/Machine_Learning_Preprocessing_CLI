import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def show_categorical_columns(data):
    print('\n{0: <20} {1}'.format("Categorical Column", "Unique Values"))
    for column in data.select_dtypes(include="object"):
        print('{0: <20} {1}'.format(column, data[column].nunique()))

def encode_column(data, column):
    encoder = OneHotEncoder(sparse=False)
    encoded_data = encoder.fit_transform(data[[column]])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names([column]))
    data = pd.concat([data, encoded_df], axis=1)
    data.drop(column, axis=1, inplace=True)
    return data

def label_encode_column(data, column):
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    return data

def fill_missing_values(data, column, strategy="mode"):
    if strategy == "mode":
        mode_value = data[column].mode()[0]
        data[column] = data[column].fillna(mode_value)
    elif strategy == "constant":
        fill_value = input(f"Enter the value to fill missing values in {column}: ")
        data[column] = data[column].fillna(fill_value)
    return data

def handle_categorical_data(data):
    tasks = [
        '1. Show Categorical Columns',
        '2. Perform One-Hot Encoding',
        '3. Perform Label Encoding',
        '4. Fill Missing Values in Categorical Columns',
        '5. Show the Dataset'
    ]

    while True:
        print("\nCategorical Data Handling Tasks")
        for task in tasks:
            print(task)

        try:
            choice = int(input("\nWhat would you like to do? (Press -1 to go back): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if choice == -1:
            break
        
        if choice == 1:
            show_categorical_columns(data)
        
        elif choice == 2:
            show_categorical_columns(data)
            column = input("Which column would you like to one-hot encode? (Press -1 to go back): ").lower()
            if column == "-1":
                continue
            if column in data.select_dtypes(include="object"):
                data = encode_column(data, column)
                print(f"One-hot encoding of {column} is done.")
            else:
                print("Invalid column name. Please try again.")
        
        elif choice == 3:
            show_categorical_columns(data)
            column = input("Which column would you like to label encode? (Press -1 to go back): ").lower()
            if column == "-1":
                continue
            if column in data.select_dtypes(include="object"):
                data = label_encode_column(data, column)
                print(f"Label encoding of {column} is done.")
            else:
                print("Invalid column name. Please try again.")

        elif choice == 4:
            show_categorical_columns(data)
            column = input("Which column would you like to fill missing values in? (Press -1 to go back): ").lower()
            if column == "-1":
                continue
            if column in data.select_dtypes(include="object"):
                strategy = input("Enter the strategy (mode/constant): ").lower()
                if strategy in ["mode", "constant"]:
                    data = fill_missing_values(data, column, strategy)
                    print(f"Missing values in {column} filled with {strategy}.")
                else:
                    print("Invalid strategy. Please try again.")
            else:
                print("Invalid column name. Please try again.")
        
        elif choice == 5:
            print(data.head())

        else:
            print("Invalid choice. Please try again.")
    
    return data


