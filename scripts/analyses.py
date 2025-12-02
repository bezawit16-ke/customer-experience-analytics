"""
Sentiment analysis and basic visualization
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

def analyze_reviews():
    # Load data
    df = pd.read_csv('../data/reviews.csv')
    
    # Sentiment analysis
    def get_sentiment(text):
        try:
            analysis = TextBlob(str(text))
            if analysis.sentiment.polarity > 0.1:
                return 'positive'
            elif analysis.sentiment.polarity < -0.1:
                return 'negative'
            else:
                return 'neutral'
        except:
            return 'neutral'
    
    df['sentiment'] = df['review'].apply(get_sentiment)
    
    # Save analyzed data
    df.to_csv('../data/analyzed_reviews.csv', index=False)
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Average rating by bank
    df.groupby('bank')['rating'].mean().plot(kind='bar', ax=axes[0,0], color='skyblue')
    axes[0,0].set_title('Average Rating by Bank')
    axes[0,0].set_ylabel('Rating')
    
    # Plot 2: Sentiment distribution
    df['sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=axes[0,1])
    axes[0,1].set_title('Overall Sentiment')
    
    # Plot 3: Reviews count by bank
    df['bank'].value_counts().plot(kind='bar', ax=axes[1,0], color='orange')
    axes[1,0].set_title('Number of Reviews by Bank')
    axes[1,0].set_ylabel('Count')
    
    # Plot 4: Rating distribution
    df['rating'].value_counts().sort_index().plot(kind='bar', ax=axes[1,1], color='green')
    axes[1,1].set_title('Rating Distribution')
    axes[1,1].set_xlabel('Rating')
    axes[1,1].set_ylabel('Count')
    
    plt.tight_layout()
    plt.savefig('../outputs/analysis_results.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Analysis complete!")
    print(f"Total reviews: {len(df)}")
    print(f"Average rating: {df['rating'].mean():.2f}")
    print(f"Sentiment: {df['sentiment'].value_counts().to_dict()}")
    
    return df

if __name__ == "__main__":
    analyze_reviews()
