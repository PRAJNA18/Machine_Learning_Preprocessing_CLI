import pandas as pd

def show_columns(data):
    print("\nColumns:\n")
    for column in data.columns.values:
        print(column, end="  ")
    print()

def download_data(data):
    to_be_downloaded = {}
    for column in data.columns.values:
        to_be_downloaded[column] = data[column]

    new_file_name = input("\nEnter the FILENAME you want (Press -1 to go back): ")
    if new_file_name == "-1":
        return
    
    new_file_name = new_file_name + ".csv"

    try:
        pd.DataFrame(data).to_csv(new_file_name, index=False)
        print(f"\nFile saved successfully as {new_file_name}.")
    except Exception as e:
        print(f"\nAn error occurred while saving the file: {e}")

    if input("\nDo you want to exit now? (y/n): ").lower() == 'y':
        print("\nExiting...")
        exit()
    else:
        return

