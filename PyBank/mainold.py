import os
import csv
import pandas as pd

# Path to collect data from the Resources folder
pybank_df = pd.read_csv('budget_data_1.csv')

# Total months can be found by count of rows
bank_months = pybank_df["Date"].count()

#format
#pybank_df["Revenue"] = pybank_df["Revenue"].map("${:,.2f}".format)

# Total Revenue
bank_rev = pybank_df["Revenue"].sum()


# Output table
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(bank_months))
print("Total Revenue: " + str(bank_rev) )