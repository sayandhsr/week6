import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv(r"C:\Users\Dell\OneDrive\Documents\devoloper arena\week6\sales_data (3).csv")

# ===============================
# CLEAN DATA
# ===============================
df.columns = df.columns.str.strip().str.lower()

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Create new columns
df['month'] = df['date'].dt.month
df['total_sales'] = df['quantity'] * df['price']

print("Columns:", df.columns)

# ===============================
# 🎨 SEABORN STYLE
# ===============================
sns.set_style("whitegrid")

# ===============================
# 📊 1. BOX PLOT
# ===============================
plt.figure()
sns.boxplot(x='product', y='total_sales', data=df)
plt.title("Sales Distribution by Product")
plt.xticks(rotation=30)
plt.savefig("boxplot.png")

# ===============================
# 📊 2. VIOLIN PLOT
# ===============================
plt.figure()
sns.violinplot(x='product', y='total_sales', data=df)
plt.title("Sales Spread by Product")
plt.xticks(rotation=30)
plt.savefig("violin.png")

# ===============================
# 📊 3. HEATMAP (CORRELATION)
# ===============================
plt.figure()
corr = df[['quantity', 'price', 'total_sales']].corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")

# ===============================
# 📊 4. SUBPLOTS (2x2 DASHBOARD)
# ===============================
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Monthly trend
monthly = df.groupby('month')['total_sales'].sum()
monthly.plot(ax=axes[0, 0], title="Monthly Sales")

# Product sales
product_sales = df.groupby('product')['total_sales'].sum()
product_sales.plot(kind='bar', ax=axes[0, 1], title="Product Sales")

# Region sales
region_sales = df.groupby('region')['total_sales'].sum()
region_sales.plot(kind='bar', ax=axes[1, 0], title="Region Sales")

# Quantity distribution
sns.histplot(df['quantity'], ax=axes[1, 1])
axes[1, 1].set_title("Quantity Distribution")

plt.tight_layout()
plt.savefig("dashboard.png")

# ===============================
# 📊 5. INTERACTIVE (PLOTLY)
# ===============================
fig = px.bar(df, x='product', y='total_sales', color='region',
             title="Interactive Product Sales")
fig.write_html("interactive_dashboard.html")

print("\n✅ All visualizations created successfully")