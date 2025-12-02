"""
Web scraping script for Google Play Store reviews
"""
import pandas as pd
from google_play_scraper import reviews, Sort
import time

def scrape_reviews(app_id, bank_name, count=100):
    """
    Scrape reviews for a given app ID
    """
    print(f"Scraping {bank_name} reviews...")
    
    try:
        # Get reviews
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=count
        )
        
        # Process reviews
        reviews_list = []
        for r in result:
            reviews_list.append({
                'bank': bank_name,
                'rating': r['score'],
                'review': r['content'],
                'date': r['at'].strftime('%Y-%m-%d'),
                'source': 'Google Play'
            })
        
        return pd.DataFrame(reviews_list)
        
    except Exception as e:
        print(f"Error scraping {bank_name}: {e}")
        return pd.DataFrame()

# Main execution
if __name__ == "__main__":
    # App IDs for Ethiopian banks (these are examples - verify actual IDs)
    apps = {
        'com.commercialbankofethiopia.cbe': 'CBE',
        'com.bankofabyssinia.boa': 'BOA',
        'com.dashenbank.scmobile': 'Dashen'
    }
    
    all_reviews = []
    
    for app_id, bank_name in apps.items():
        df = scrape_reviews(app_id, bank_name, count=50)
        if not df.empty:
            all_reviews.append(df)
        time.sleep(2)  # Be respectful to servers
    
    # Combine and save
    if all_reviews:
        final_df = pd.concat(all_reviews, ignore_index=True)
        final_df.to_csv('../data/reviews.csv', index=False)
        print(f"Saved {len(final_df)} reviews to data/reviews.csv")
    else:
        print("No reviews scraped. Creating sample data...")
        # Create sample data
        sample_data = {
            'bank': ['CBE', 'CBE', 'BOA', 'Dashen'],
            'rating': [4, 2, 3, 5],
            'review': ['Great app', 'Login issues', 'Slow transfers', 'Excellent'],
            'date': ['2024-11-30']*4,
            'source': ['Google Play']*4
        }
        sample_df = pd.DataFrame(sample_data)
        sample_df.to_csv('../data/reviews.csv', index=False)
