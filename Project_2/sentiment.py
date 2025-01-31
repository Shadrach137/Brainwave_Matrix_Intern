#Import relevant libraries
import pandas as pd
import re
import emoji
from textblob import TextBlob

# Function to clean text
def clean_text(text):
    # Handle NaN values
    if isinstance(text, float):
        return ""
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    # Remove mentions and hashtags
    text = re.sub(r"@\w+|#\w+", "", text)
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Convert emojis to text
    text = emoji.demojize(text)
    # Remove extra whitespaces
    text = re.sub(r"\s+", " ", text).strip()
    # Convert to lowercase
    text = text.lower()
    return text

# Function to calculate sentiment polarity
def analyze_sentiment(text):
    # Ensure valid input
    if isinstance(text, str) and text.strip():
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
    # Neutral sentiment for empty/invalid text
    return 0

# Process Samsung comments
samsung_df = pd.read_csv("YouTube_Samsung_Comments_with_Cleaned_Timestamps.csv")
samsung_df['Cleaned_Comment'] = samsung_df['Comment'].apply(clean_text)
samsung_df['Sentiment'] = samsung_df['Cleaned_Comment'].apply(analyze_sentiment)
samsung_df.to_csv("Samsung_Sentiment_Final.csv", index=False)

# Process Pixel comments
pixel_df = pd.read_csv("YouTube_Pixel_Comments_with_Cleaned_Timestamps.csv")
pixel_df['Cleaned_Comment'] = pixel_df['Comment'].apply(clean_text)
pixel_df['Sentiment'] = pixel_df['Cleaned_Comment'].apply(analyze_sentiment)
pixel_df.to_csv("Pixel_Sentiment_Final.csv", index=False)

# Process iPhone comments
iphone_df = pd.read_csv("YouTube_iPhone_Comments_with_Cleaned_Timestamps.csv")
iphone_df['Cleaned_Comment'] = iphone_df['Comment'].apply(clean_text)
iphone_df['Sentiment'] = iphone_df['Cleaned_Comment'].apply(analyze_sentiment)
iphone_df.to_csv("iPhone_Sentiment_Final.csv", index=False)

print("Sentiment analysis completed. Cleaned and sentiment-scored files saved!")
