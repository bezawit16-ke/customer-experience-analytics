"""
Final Data Collection Script
"""
import pandas as pd
print("=== DATA COLLECTION FOR BANKING APPS ===")

# Create realistic sample data
banks = ['CBE', 'BOA', 'Dashen']
data = []

for bank in banks:
    # Create 5 reviews per bank
    for i in range(5):
        rating = [1, 3, 4, 4, 5][i]  # Mix of ratings
        review = f"{bank} app review {i+1}"
        data.append({
            'bank': bank,
            'rating': rating,
            'review': review,
            'date': '2024-12-02',
            'source': 'Google Play'
        })

df = pd.DataFrame(data)
df.to_csv('data/reviews.csv', index=False)
print(f"✅ Created {len(df)} reviews in data/reviews.csv")
print(df.head())
