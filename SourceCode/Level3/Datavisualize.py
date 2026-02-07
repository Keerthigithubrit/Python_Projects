# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
sales_data = pd.read_csv(r"C:\Users\Welcome\Desktop\Python_Intern_Task\Sales_data.csv")

# convert date column into datetime
sales_data["Date"] = pd.to_datetime(sales_data["Date"])

# Visualize settings
sns.set_theme(style = "white")
plt.rcParams["figure.figsize"] = (8,5)

# 1.Total Sales by Product line
plt.figure()
sns.barplot(data =sales_data, x="Product line", y="Total", estimator= sum,hue="City", palette="coolwarm",legend= False)
plt.title("Total Sales by ProductLine")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Branch_wise Total Revenue
plt.figure()
sns.barplot(data=sales_data, x="Branch", y="Total", estimator=sum, hue="City", palette="coolwarm", legend= False)
plt.title("Total Revenge by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

# 3. Daily Sales Trend
daily_sales = sales_data.groupby("Date")["Total"].sum().reset_index()
plt.figure()
sns.lineplot(data=daily_sales, x="Date", y="Total", marker="o")
plt.title("Daily Sales trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# 4. Sales Distribution
plt.figure()
sns.histplot(sales_data["Total"])
plt.title("Distribution of Total Sales")
plt.xlabel("Total sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 5. Payment Method distribution
plt.figure()
sns.countplot(data=sales_data, x="Payment",hue="Customer type", palette="Set2")
plt.title("payment Method Usage")
plt.xlabel("payment Method")
plt.ylabel("Number of Tranactions")
plt.tight_layout()
plt.show()

# 6. Gender wise sales comparision
plt.figure()
sns.barplot(data=sales_data, x="Gender", y="Total", hue="City",palette="coolwarm")
plt.title("Gender_wise Sales Distribution")
plt.xlabel("Gender")
plt.ylabel("total Sales")
plt.tight_layout()
plt.show()

# 7.Monthly sales Trend
monthly_sales = sales_data.groupby("Month")["Total"].sum().reset_index()
plt.figure()
sns.lineplot(data=monthly_sales, x="Month", y="Total", marker="o")
plt.xlabel("Month")
plt.ylabel("total sales")
plt.tight_layout()
plt.show()