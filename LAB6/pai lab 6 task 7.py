import pandas as pd
df= pd.read_excel(r"C:/Users/hamza/Downloads/Employee-Management-Sample-Data.xlsx")
employees=df["Full Name"]
print(employees)