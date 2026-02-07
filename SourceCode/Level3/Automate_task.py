# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Dataset
sales_data = pd.read_csv(r"C:\Users\Welcome\Desktop\Python_Intern_Task\Sales_data.csv")

# convert date column to datetime
sales_data["Date"] = pd.to_datetime(sales_data["Date"])

# Create output folder if doesnot exists
output_folder = "Report"
os.makedirs(output_folder, exist_ok=True)

# Automation settings
sns.set_theme(style= "white")
plt.rcParams["figure.figsize"] =(8,5)

# Automated DataPreprocessing
daily_sales = sales_data.groupby("Date").agg(
    Total_Sales = ("Total","sum"),
    Total_Quantity=("Quantity","sum"),
    Average_Rating=("Rating","mean")
).reset_index()

# Save Automated Report in folder
report_path = os.path.join(output_folder, "Daily_Sales_Report.csv")
daily_sales.to_csv(report_path, index=False)
print("Daily Sales Report generated successfully!")

# Automated Visualization
plt.figure()
sns.lineplot(data=daily_sales, x="Date", y="Total_Sales", marker="o")
plt.title("Automated Daily sales Report")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()

# Save plot in folder
plot_path = os.path.join(output_folder, "Daily_Sales_Trend.png")
plt.savefig(plot_path)
plt.close()
print("Sales Trend chart saved Successfully!")