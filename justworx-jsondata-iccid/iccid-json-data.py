import pandas as pd
import json

# Read the CSV file into a DataFrame with no header
input_file_path = "IN106260.csv"
df = pd.read_csv(input_file_path, header=None)

# ICCID List
iccid_list = df.iloc[:, 0].tolist()


# Constant fields
Client_name = "Midcity"
Plan = "Data4Life 10MB"

# Create a list to store JSON objects
json_data = {
    "sims": []
}

# count var to id line where ICCID is incorrect.
count = 0

# Iterate through the ICCID list and create JSON objects
for iccid in iccid_list:
    
    # Test iccid length to confirm if iccid is valid
    # Check if length of each ICCID == 19  is TRUE
    
    if len(str(iccid)) == 19:
        count += 1
    else: print("iccid length incorrect on line:", count+1, "in .csv file")
    

    data = {
        "name": Client_name,
        "iccid": str(iccid),
        "provider": 1,
        "simPlan": Plan,
        "sites": [
            {
                "id": 7,
                "name": "Riecktron"
            }
        ]
    }
    json_data["sims"].append(data)

print("Number of ICCID's =", len(iccid_list))

# Convert the JSON data to a JSON string
json_string = json.dumps(json_data, indent=2)

# Print the JSON string
#print(json_string[:300])

# Save the JSON string to a text file
output_file_path = "IN106260.json"
with open(output_file_path, "w") as output_file:
    output_file.write(json_string)

print(f"JSON data saved to {output_file_path}")
