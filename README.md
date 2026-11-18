# Retail Transaction Data Cleaning and Sales Analysis

## Project Overview

This project focuses on cleaning and analyzing retail transaction data to understand sales performance, discount patterns, household purchasing behavior, and basket-level sales metrics. Using Python, Pandas, and NumPy, the project performs data loading, data type optimization, discount calculations, statistical analysis, data aggregation, and identification of top-performing households.

The analysis explores transaction-level sales, total discounts, purchase quantities, average sales per basket, and household purchasing patterns.

## Key Features

- Loading retail transaction data using Pandas
- Selecting relevant columns from the transaction dataset
- Inspecting dataset information and data types
- Converting numerical columns into appropriate integer data types
- Calculating total discounts for each transaction
- Calculating percentage discounts
- Limiting discount percentages between 0 and 1
- Removing unnecessary individual discount columns
- Calculating total sales value
- Calculating total discount value
- Calculating total quantity sold
- Identifying maximum quantity purchased in a single transaction
- Calculating sales value per basket
- Calculating sales value per household
- Identifying the top 10 households by quantity purchased
- Identifying the top 10 households by sales value
- Exporting cleaned transaction data into a new CSV file

## Dataset Overview

The project uses the `project_transactions.csv` dataset.

The analysis selects the following columns:

| Column | Description |
|---|---|
| household_key | Unique household identifier |
| BASKET_ID | Unique transaction basket identifier |
| DAY | Day of the transaction |
| PRODUCT_ID | Unique product identifier |
| QUANTITY | Number of units purchased |
| SALES_VALUE | Sales value of the transaction |
| RETAIL_DISC | Retail discount applied |
| COUPON_DISC | Coupon discount applied |
| COUPON_MATCH_DISC | Coupon matching discount |

## Data Cleaning and Transformation

### Data Type Optimization

The project converts selected columns into 32-bit integer data types:

- DAY – int32
- QUANTITY – int32
- PRODUCT_ID – int32

This helps optimize numerical data representation.

### Discount Calculation

Two additional columns are created:

- **Total Discount:** Absolute sum of retail discount and coupon discount.
- **Percentage Discount:** Total discount divided by sales value.

The percentage discount is restricted to a range between 0 and 1 using the Pandas `clip()` function.

The individual discount columns are then removed from the cleaned dataset.

## Sales Performance Analysis

The project calculates several important sales metrics:

- Total Sales – Sum of all transaction sales values.
- Total Discount – Sum of calculated transaction discounts.
- Total Quantity Sold – Sum of purchased quantities.
- Sales Value per Basket – Total sales divided by the number of unique baskets.
- Sales Value per Household – Total sales divided by the number of unique households.

These calculations help summarize overall retail transaction performance.

## Household Purchasing Analysis

The project performs household-level aggregation to identify purchasing patterns.

Two major analyses are performed:

1. **Top 10 Households by Quantity Purchased:** Identifies households with the highest total purchase quantities.
2. **Top 10 Households by Sales Value:** Identifies households generating the highest total sales value.

The project also identifies the transaction row with the maximum purchase quantity for further inspection of its discount percentage.

## Technologies Used

- Python – Programming language used for data processing and analysis.
- Jupyter Notebook / Python Environment – Environment for executing the analysis.

## Libraries Used

| Library | Purpose |
|---|---|
| Pandas | Reading CSV files, data cleaning, data type conversion, discount calculations, grouping, aggregation, and exporting cleaned data. |
| NumPy | Supporting numerical operations and data analysis. |

## Project Files

- Project_1.py – Python script containing the complete data cleaning and analysis workflow.
- project_transactions.csv – Original retail transaction dataset.
- cleaned_transactions.csv – Exported cleaned transaction dataset.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### 2. Install Required Libraries

```bash
pip install pandas numpy
```

### 3. Add the Dataset

Place `project_transactions.csv` in the project directory.

### 4. Run the Python Script

```bash
python Project_1.py
```

### 5. View the Output

After successful execution, the project generates:

```text
cleaned_transactions.csv
```

The exported CSV file contains the processed transaction data and calculated sales and discount metrics.

**Note:** Ensure that the dataset file is available in the expected project directory, or update the file path in the Python script before execution.
