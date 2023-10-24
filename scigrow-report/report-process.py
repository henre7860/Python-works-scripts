import pandas as pd

# Input and output file names
file_name_input = "forestmews-1oct2022-1oct2023.xlsx"
file_name_output = "forestmews-1oct2022-1oct2023-output.xlsx"

# Read the input Excel file into a DataFrame
df = pd.read_excel(file_name_input)

# Define the start and end months for column renaming and processing
start_month = "1 October 2022"
end_month = "1 October 2023"

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
