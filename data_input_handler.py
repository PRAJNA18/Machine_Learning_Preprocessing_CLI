import sys
import pandas as pd
from os import path

def change_to_lower_case(data):
    return data.rename(columns=lambda x: x.lower())

def input_function():
    try:
        filename, file_extension = path.splitext(sys.argv[1])
        if file_extension == "":
            raise SystemExit("Please provide the dataset name (with extension).")

        supported_file_extensions = ['.csv']
        if file_extension not in supported_file_extensions:
            raise SystemExit("This file extension is not supported.")
    
    except IndexError:
        raise SystemExit("Please provide the dataset name (with extension).")
    
    try:
        data = pd.read_csv(filename + file_extension)
    except pd.errors.EmptyDataError:
        raise SystemExit("The file is empty.")

    except FileNotFoundError:
        raise SystemExit("File doesn't exist.")

    data = change_to_lower_case(data)

    return data


