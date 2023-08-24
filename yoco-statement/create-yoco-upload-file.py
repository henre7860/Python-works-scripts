import pandas as pd

def process_yoco_data(input_file_path, output_file_name):
    # Read the CSV file into a DataFrame, skipping the first row (header)
    df = pd.read_csv(input_file_path, skiprows=1)

    # Add new columns to the DataFrame
    df["Amount"] = df["Total (incl. tax)"]
    df["Reference Number"] = df["Note"]
    df["Description"] = None

    # Specify columns to keep in the DataFrame
    columnsToKeep = ["Date", "Description", "Reference Number", "Amount", "Fee Amount"]

    # Filter the DataFrame to retain only specified columns
    df = df[columnsToKeep]

    # Make the "Fee Amount" values negative
    df.loc[:, "Fee Amount"] = df["Fee Amount"] * -1

    # Create a list to store modified rows
    new_rows = []

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Check if "Fee Amount" is not equal to zero
        if row['Fee Amount'] != 0:
            # Create a copy of the row and modify values
            new_row = row.copy()
            new_row['Description'] = 'yoco fee'
            new_row['Amount'] = row['Fee Amount']
            # Add the modified row to the list
            new_rows.append(new_row)

    # Create a new DataFrame from the modified rows
    new_df = pd.DataFrame(new_rows)

    # Concatenate the original DataFrame and the new DataFrame
    result_df = pd.concat([df, new_df], ignore_index=True)

    # Specify columns to keep in the new DataFrame
    columnsToKeep = ["Date", "Description", "Reference Number", "Amount"]

    # Filter the concatenated DataFrame to retain specified columns
    df2 = result_df[columnsToKeep]

    return df2

# Define the path to the input CSV file
yoco_input = "Transactions-from-2023-08-01.csv"
    
# Define the output file name for the CSV
yoco_output = "yoco-output.csv"

# Process the data and get the processed DataFrame
df = process_yoco_data(yoco_input, yoco_output)

# Print the processed DataFrame
print(df)

# Export the processed DataFrame to a CSV file without the index column
df.to_csv(yoco_output, index=None)
