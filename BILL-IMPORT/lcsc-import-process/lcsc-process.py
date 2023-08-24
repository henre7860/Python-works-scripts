import pandas as pd
inputFileName = "LCSC_Exported__20230823_203921.csv"

df = pd.read_csv(inputFileName)

columnsToKeep = ['Manufacture Part Number', 'Description', 'Order Qty.', 'Unit Price','Order Price']
df2 = df[columnsToKeep]

totalZAR = 10000
totalUSD = 1756.07
ZARUSD = round(totalZAR / totalUSD,5)
print("ZARUSD =", ZARUSD)

totalUSDCalculate = round(sum(df2.loc[:, "Order Price"]),6)
print("Total USD input = Total calulated USD:",totalUSDCalculate == totalUSD)

df2["Unit Price (ZAR)"] = round(df2["Unit Price"] * ZARUSD,6)

df2["Order Price (ZAR)"] = df2["Order Qty."] * df2["Unit Price (ZAR)"] 

totalZARCalculate = round(sum(df2.loc[:, "Order Price (ZAR)"]), 6)
print("Total ZAR input = Total calulated ZAR:",totalZARCalculate == totalZAR)
print("Total ZAR =", totalZARCalculate)

columnsOrder = ['Manufacture Part Number', 'Description', 'Order Qty.', 'Unit Price', 'Unit Price (ZAR)','Order Price','Order Price (ZAR)']

output_df = df2[columnsOrder]
outpuFileName = "lcsc-ouput-test.csv"

output_df.to_csv(outpuFileName, index= None)