"""
Final Analysis Script
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== FINAL ANALYSIS ===")

# Load data
df = pd.read_csv('data/reviews.csv')
print(f"📊 Loaded {len(df)} reviews")

# Create outputs folder
import os
os.makedirs('outputs', exist_ok=True)

# Plot 1: Average rating
plt.figure(figsize=(10, 6))
avg_ratings = df.groupby('bank')['rating'].mean()
avg_ratings.plot(kind='bar', color=['blue', 'green', 'orange'])
plt.title('Average Rating by Bank')
plt.ylabel('Rating (1-5)')
plt.ylim(0, 5)
plt.grid(True, alpha=0.3)
plt.savefig('outputs/avg_ratings.png', dpi=300, bbox_inches='tight')

# Plot 2: Rating distribution
plt.figure(figsize=(10, 6))
rating_counts = df['rating'].value_counts().sort_index()
rating_counts.plot(kind='bar', color='purple')
plt.title('Overall Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.savefig('outputs/rating_dist.png', dpi=300, bbox_inches='tight')

# Plot 3: Reviews per bank
plt.figure(figsize=(10, 6))
bank_counts = df['bank'].value_counts()
bank_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Reviews Distribution by Bank')
plt.savefig('outputs/bank_dist.png', dpi=300, bbox_inches='tight')

print("✅ Created 3 visualizations in outputs/ folder")
print(f"Average ratings:\n{avg_ratings}")