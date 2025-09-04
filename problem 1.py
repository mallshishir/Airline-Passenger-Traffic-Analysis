import pandas as pd   # ✅ Add this at the top
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("flights.csv")

# Create datetime column
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'], format='%Y-%B')

# Sort values by date
df = df.sort_values('date')

# Plot
plt.figure(figsize=(12,6))
plt.plot(df['date'], df['passengers'], marker='o')
plt.title("Monthly Passenger Traffic Trend")
plt.xlabel("Date")
plt.ylabel("Passengers")
plt.grid(True)
plt.show()




# ---------------- Q2 ----------------
# Group by month across all years
month_order = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]

monthly_totals = df.groupby('month')['passengers'].sum().reindex(month_order)

# Plot passenger vs month (total across years)
plt.figure(figsize=(12,6))
plt.plot(monthly_totals.index, monthly_totals.values, marker='o', color='orange')
plt.title("Total Passenger Traffic by Month (1949–1960 Combined)")
plt.xlabel("Month")
plt.ylabel("Total Passengers (All Years)")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
