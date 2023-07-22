import os
import pandas as pd

# Get the current folder name
current_folder_name = os.path.basename(os.getcwd())

# Get all excel files in the current directory
excel_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.xlsx') or f.endswith('.xls')]

# Loop through each excel file
for file in excel_files:
    try:
        # Load the excel file
        df = pd.read_excel(file)

        # Get the first cell value
        first_cell_value = df.iloc[0, 0]

        # Create a description with a placeholder
        description = f"The {current_folder_name} contains data about a dinosaur named {first_cell_value}. This data is found in the file named {file}."

        # Print the description
        print(description)

    except Exception as e:
        print(f"An error occurred when processing file {file}: {e}")
