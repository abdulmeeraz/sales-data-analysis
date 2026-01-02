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

    # Calculate average sales per transaction
    average_sales = sales_data["Total_sales"].mean()
    print(f"Average Sales per Transaction : ${average_sales:.2f}")

    # Best-selling product
    best_selling_product = sales_data.groupby("Product")["Total_sales"].sum().idxmax()
    print(f"Best-Selling Product : {best_selling_product}")

    # Sales by category
    sales_by_category = sales_data.groupby("Category")["Total_sales"].sum()
    print("\n--- Sales by Category ---")
    print(sales_by_category)
    



sales_analysis()