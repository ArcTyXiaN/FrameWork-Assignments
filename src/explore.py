import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Step 1: Load dataset
# ==============================
df = pd.read_csv("data/sample_metadata.csv")
print("Original shape:", df.shape)
print(df.head())

# ==============================
# Step 2: Clean dataset
# ==============================
# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Create a new column for year
df['year'] = df['publish_time'].dt.year

# Fill missing journal values with "Unknown"
df['journal'] = df['journal'].fillna("Unknown")

# Drop rows without title or publish_time
df = df.dropna(subset=["title", "publish_time"])

print("\nAfter cleaning, shape:", df.shape)
print(df.info())

# Save cleaned dataset
df.to_csv("data/sample_metadata_clean.csv", index=False)
print("\nCleaned dataset saved as data/clean_sample.csv")

# ==============================
# Step 3: Visualizations
# ==============================

# Publications by year
year_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values)
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Publications by Year")
plt.show()

# Top 5 journals
top_journals = df['journal'].value_counts().head(5)

plt.figure(figsize=(8, 5))
plt.bar(top_journals.index, top_journals.values)
plt.xticks(rotation=45, ha='right')
plt.ylabel("Number of Papers")
plt.title("Top 5 Journals")
plt.show()
