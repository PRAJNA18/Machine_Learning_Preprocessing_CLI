# main_script.py
from data_description_tool import describe_dataset
from data_input_handler import input_function
from data_imputer import imputer
from dataset_encoder import handle_categorical_data
from dataset_scaler import feature_scaling
from dataset_downloader import download_data

def ml_preprocessor_cli():
    dataset = input_function()
    print("\n\nMachine Learning Preprocessor CLI!\n\n")

    print("Attributes:")
    for attribute in dataset.columns.values:
        print(attribute, end="  ")

    while True:
        print("\nPreprocessing Tasks:\n")
        print("1. Describe Dataset")
        print("2. Handle Missing Values")
        print("3. Encode Categorical Features")
        print("4. Scale Features")
        print("5. Download Processed Dataset")
        print("-1. Exit")

        while True:
            try:
                choice = int(input("\nPlease enter your choice (Enter -1 to exit): "))
            except ValueError:
                print("Invalid input. Please enter an integer value.")
                continue
            break

        if choice == -1:
            exit()

        elif choice == 1:
            describe_dataset(dataset)

        elif choice == 2:
            dataset = imputer(dataset)

        elif choice == 3:
            dataset = handle_categorical_data(dataset)

        elif choice == 4:
            dataset = feature_scaling(dataset)

        elif choice == 5:
            download_data(dataset)

        else:
            print("\nInvalid choice. Please try again..")

ml_preprocessor_cli()
