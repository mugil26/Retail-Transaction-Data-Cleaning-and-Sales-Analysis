import pandas as pd
import numpy as np

#First, read in the transactions data.
#Read in the only columns household_key, BASKET_ID, DAY, PRODUCT_ID, QUANTITY, and SALES_VALUE.
df=pd.read_csv("./project_transactions.csv",usecols=['household_key', 'BASKET_ID', 'DAY', 'PRODUCT_ID', 'QUANTITY','SALES_VALUE','RETAIL_DISC','COUPON_DISC','COUPON_MATCH_DISC'])
print(df.info())

# Convert DAY, QUANTITY, and PRODUCT_ID to the smallest appropriate integer types. (Typecase into int32).
NewDay=df['DAY'].astype('int32')
NewQunatity=df['QUANTITY'].astype('int32')
NewProduct=df['PRODUCT_ID'].astype('int32')
# print(df.info())

# A column that captures the total_discount by row (sum of RETAIL_DISC, COUPON_DISC).
df['total_discount']=(df['RETAIL_DISC']+df['COUPON_DISC']).abs()
# print(df['total_discount'])

#The percentage disount (total_discount / SALES_VALUE). Make sure this is positive (try .abs()).
df['Percentage_discount']=(df['total_discount']/df['SALES_VALUE']).abs()
# print(df['Percentage_discount'])

#If the percentage discount is greater than 1, set it equal to 1. If it is less than 0, set it to 0. 
df['Percentage_discount']=df['Percentage_discount'].clip(0,1)

#Drop the individual discount columns (RETAIL_DISC, COUPON_DISC, COUPON_MATCH_DISC).
df=df.drop(columns=['RETAIL_DISC','COUPON_DISC','COUPON_MATCH_DISC'])

#The total sales (sum of SALES_VALUE)
df['total_sales']=df['SALES_VALUE'].sum()
# print(df['total_sum'])

#Total discount (sum of total_discount)
df['total_discount']=df['total_discount'].sum()
#print(df['total_discount'])

#Overall percentage discount (sum of total_discount / sum of sales value)
df['Percentage_discount']=df['total_discount']/df['SALES_VALUE']
#print(df['Percentage_discount'])

#Total quantity sold (sum of QUANTITY).
df['Total_quantity']=df['QUANTITY'].sum()
#print(df['Total_quantity'])

#Max quantity sold in a single row. Inspect the row as well. Does this have a high discount percentage?
max_quantity=df['QUANTITY'].max()

max_quantity_row=df.loc[df['QUANTITY'].idxmax()]
#print(max_quantity_row)

#Total sales value per basket (sum of sales value / nunique basket_id).
df['value_per_basket']=df['total_sales']/ df['BASKET_ID'].nunique()
#print(df['value_per_basket'])

#Total sales value per household (sum of sales value / nunique household_key).
df['total_sales_per_household']=df['total_sales']/ df['household_key'].nunique()

#What were the top 10 households by quantity purchased?
top_10_households_quantity=df.groupby('household_key')['QUANTITY'].sum().nlargest(10)

#What were the top 10 households by sales value?
top_10_households_sales=df.groupby('household_key')['SALES_VALUE'].sum().nlargest(10)

#Exporting the cleaned data to a new CSV file.
df.to_csv("cleaned_transactions.csv",index=False)