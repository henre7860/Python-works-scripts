import pandas as pd

# Input and output file names
file_name_input = "forestmews-raw-data-Aug.xlsx"
file_name_output = "forestmews-raw-data-Aug-output.xlsx"

# Read the input Excel file into a DataFrame
df = pd.read_excel(file_name_input)

# Define the start and end months for column renaming and processing
start_month = "1 August 2023"
end_month = "1 September 2023"

# Get the current column names
current_columns = df.columns.tolist()

# Create new column names based on column indices and update DataFrame columns
new_columns = current_columns[:2] + [start_month, end_month] + current_columns[4:]
df.columns = new_columns

# Process specific columns (including start_month, end_month, and "Total Consumption")
for column in [start_month, end_month, "Total Consumption"]:
    # Replace " kWh" and commas, then convert to float
   
    df[column] = df[column].str.replace(' kWh', '').str.replace(',', '').astype(float)

# Export the cleaned DataFrame to an Excel file
df.to_excel(file_name_output, index=False)

# Print a success message
print("Report successfully processed")
