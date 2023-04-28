import pandas as pd
from datetime import datetime
import os

csv_file_dir = "/opt/airflow/dags/datasets/example/"

def check_csv(file_path):
    # Check if the specified file path exists
    if os.path.exists(file_path):
        # Read the contents of the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)
        # Print a message indicating that the file was found
        print(f"Checking if '{file_path}' is saved")
        print(" ")
        print("File Found: Below is the content")
        # Print the contents of the DataFrame
        print(df)
    else:
        # Print a message indicating that the file does not exist
        print(f"CSV file '{file_path}' does not exist")


if __name__ == '__main__':
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d %H-%M")
    filename = f"testfile_{date_string}.csv"
    file_path = os.path.join(csv_file_dir, filename)
    check_csv(file_path)
    print(" ")
    print("Process is done")
else:
    print('Not executed')
