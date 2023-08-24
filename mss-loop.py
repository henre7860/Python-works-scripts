import pandas as pd
start = 51947
total = 402

remove_list = [51964, 51965, 51966, 51967, 52011, 52012, 52013, 52014, 52015, 52016]

count = 0
mss = []

while count <= total + len(remove_list) - 1:
	
	next = start + count
	
	count +=1
	mss.append(next)

mss_exclude = [("MSS-00" + str(i)) for i in mss if i not in remove_list]

for sn in mss_exclude:
	print(sn)

print("\nTotal =", len(mss_exclude))

# Save the iccid list a text file
#output_file_path = "mss-outout.csv"
#
#df = pd.DataFrame(mss)
#df.to_csv(output_file_path, index=False, header=False)
#print(f"MSS data saved to {output_file_path}")
