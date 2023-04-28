# -*- coding: utf-8 -*-
""" 
A function that exchanges the value of X and Y save it to a file, use airflow to run it every 5 mintes, checks if the output is saved.
"""
import pandas as pd
from datetime import datetime
import os

# Set directory for CSV file output
csv_file_dir = "/opt/airflow/dags/datasets/example/"

# Function to exchange values of x and y
def exchange_values():
    x = 100
    y = 12
    print("Before exchange: x=", x, " y=", y)
    x, y = y, x
    print("After exchange: x=", x, " y=", y)
    return x, y

# Function to save exchanged values to CSV file
def save_to_csv(file_path):
    x, y = exchange_values()
    df = pd.DataFrame({'x': [x], 'y': [y]})
    df.to_csv(file_path, index=False)
    print(" ")
    print('Output saved to CSV file:', file_path)

# Main block of code
if __name__ == '__main__':
    # Get current date and time
    now = datetime.now()
    # Format date and time as string for filename
    date_string = now.strftime("%Y-%m-%d %H-%M")
    # Construct full file path with filename
    filename = f"testfile_{date_string}.csv"
    file_path = os.path.join(csv_file_dir, filename)
    # Save exchanged values to CSV file
    save_to_csv(file_path)
    print(" ")
    print("Process is done")
else:
    print('Not executed')
