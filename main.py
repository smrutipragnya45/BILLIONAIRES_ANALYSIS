import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Billionaire.csv")
data = data.dropna()

# Clean NetWorth column
data["NetWorth"] = data["NetWorth"].str.strip("$").str.strip("B").astype(float)

# Histogram of Top 10 Billionaires by NetWorth (no changes here)
df = data.sort_values(by=["NetWorth"], ascending=False).head(10)
plt.figure(figsize=(20, 10))
sns.histplot(x="Name", hue="NetWorth", data=df)
plt.title("Top 10 Billionaires by Net Worth")
plt.show()

### PIE CHARTS WITH PERCENTAGE LABELS

# Top 5 Domains to Become a Billionaire
a = data["Source"].value_counts().head()
index = a.index
sources = a.values
colors = ["skyblue", "yellowgreen", "tomato", "blue", "red"]
plt.figure(figsize=(6, 6))
plt.pie(sources, labels=index, colors=colors, autopct='%1.1f%%', startangle=140)
plt.gca().add_artist(plt.Circle((0, 0), 0.5, color='white'))  # Donut center
plt.title("Top 5 Domains to Become a Billionaire", fontsize=16)
plt.tight_layout()
plt.show()

# Top 5 Industries with Most Billionaires
a = data["Industry"].value_counts().head()
index = a.index
industries = a.values
plt.figure(figsize=(6, 6))
plt.pie(industries, labels=index, colors=colors, autopct='%1.1f%%', startangle=140)
plt.gca().add_artist(plt.Circle((0, 0), 0.5, color='white'))
plt.title("Top 5 Industries with Most Billionaires", fontsize=16)
plt.tight_layout()
plt.show()

# Top 5 Countries with Most Billionaires
a = data["Country"].value_counts().head()
index = a.index
countries = a.values
plt.figure(figsize=(6, 6))
plt.pie(countries, labels=index, colors=colors, autopct='%1.1f%%', startangle=140)
plt.gca().add_artist(plt.Circle((0, 0), 0.5, color='white'))
plt.title("Top 5 Countries with Most Billionaires", fontsize=16)
plt.tight_layout()
plt.show()
