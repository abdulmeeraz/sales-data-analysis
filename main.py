import pandas as pd


def sales_analysis():

    # Load sales data from CSV file
    sales_data = pd.read_csv('sales.csv')

    sales_data["Total_sales"] = sales_data["Quantity"] * sales_data["Unit_Price"]

    # Display sales data
    print("--- Sales Data ---") 
    print(sales_data)

    # Display summary statistics
    print("\n--- Summary Statistics ---")
    print(sales_data.describe())

    # Calculate total sales
    total_salesf = sales_data["Total_sales"].sum()
    print(f"Total Sales : ${total_salesf:.2f}")



sales_analysis()