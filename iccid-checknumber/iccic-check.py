import pandas as pd
import math

# Read the CSV file into a DataFrame with no header
input_file_path = "iccid-gas.csv"
df = pd.read_csv(input_file_path, header=None)

# ICCID List
iccid_list = df.iloc[:, 0].tolist()

def full_iccid(first):
    first_string = str(first)
    f_split = [int(i) for i in first_string]

    
    for i in range(len(f_split)):
        if i%2 == 1:
            f_split[i] *=2
            if f_split[i] > 9:
                f_split[i] -= 9

    
    f_sum = sum(f_split)
    digit = math.ceil(f_sum/10) *10 - f_sum

    iccid = str(first) + str(digit)


    return iccid

iccid_calc = []
for i in range(len(iccid_list)):
    iccid = full_iccid(iccid_list[i])
    iccid_calc.append(int(iccid))
    



# Save the iccid list a text file
output_file_path = "iccid-gas-outout.csv"

df = pd.DataFrame(iccid_calc)
df.to_csv(output_file_path, index=False, header=False)

