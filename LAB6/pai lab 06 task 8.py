import pandas as pd
productdata=pd.read_csv("products.csv")
ordersdata=pd.read_csv("orders.csv")
print(productdata.head(5))
print(productdata.tail(10))
print(ordersdata.head(5))
print(ordersdata.tail(10))
merged=pd.merge(productdata,ordersdata, on="ProductID")
merged["revenue"]=merged["Quantity"]* merged["Price"]
total=merged["revenue"].sum()
print(total)
product_sales = merged.groupby(['ProductID', 'Category'])['Quantity'].sum().reset_index()

top_selling_products = product_sales.nlargest(5, 'Quantity')

category_counts = top_selling_products['Category'].value_counts()

most_common_category = category_counts.idxmax()
most_common_count = category_counts.max()


print("Most Common Product Category among Top 5 Best-Selling Products:", most_common_category)
print("Number of Products in this Category:", most_common_count)


average_price_per_category = merged.groupby('Category')['Price'].mean().reset_index()

print("Average Price of Products in Each Category:")
print(average_price_per_category)