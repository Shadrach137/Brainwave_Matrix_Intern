#Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import emoji

# Load the cleaned datasets
samsung_df = pd.read_csv("YouTube_Samsung_Comments_with_Cleaned_Timestamps.csv")
pixel_df = pd.read_csv("YouTube_Pixel_Comments_with_Cleaned_Timestamps.csv")
iphone_df = pd.read_csv("YouTube_iPhone_Comments_with_Cleaned_Timestamps.csv")

# Combine all datasets for easier comparison
df = pd.concat([samsung_df[['Cleaned_Comment', 'Sentiment']],
                pixel_df[['Cleaned_Comment', 'Sentiment']],
                iphone_df[['Cleaned_Comment', 'Sentiment']]])

df['Device'] = ['Samsung'] * len(samsung_df) + ['Pixel'] * len(pixel_df) + ['iPhone'] * len(iphone_df)

# Set the style for Seaborn
sns.set(style="whitegrid")

# Sentiment Distribution Plot
plt.figure(figsize=(10, 6))
sns.histplot(df['Sentiment'], bins=30, kde=True, color='blue', stat='density', label="Sentiment Distribution")
plt.title('Sentiment Distribution of Comments')
plt.xlabel('Sentiment Score')
plt.ylabel('Density')
plt.legend()
plt.show()

# Average Sentiment by Device
plt.figure(figsize=(8, 6))
sns.boxplot(x='Device', y='Sentiment', data=df, hue='Device', palette="coolwarm", dodge=False, legend=False)
plt.title('Average Sentiment Score by Device')
plt.xlabel('Device')
plt.ylabel('Sentiment Score')
plt.show()

# Emoji Count Visualization
# Updated to work with the latest emoji library
def count_emojis(text):
    return sum(1 for c in str(text) if emoji.is_emoji(c))

samsung_df['Emoji_Count'] = samsung_df['Cleaned_Comment'].apply(count_emojis)
pixel_df['Emoji_Count'] = pixel_df['Cleaned_Comment'].apply(count_emojis)
iphone_df['Emoji_Count'] = iphone_df['Cleaned_Comment'].apply(count_emojis)

# Combine emoji counts into a new DataFrame
emoji_df = pd.concat([samsung_df[['Emoji_Count']],
                      pixel_df[['Emoji_Count']],
                      iphone_df[['Emoji_Count']]])

emoji_df['Device'] = ['Samsung'] * len(samsung_df) + ['Pixel'] * len(pixel_df) + ['iPhone'] * len(iphone_df)

plt.figure(figsize=(8, 6))
sns.boxplot(x='Device', y='Emoji_Count', data=emoji_df, hue='Device', palette="pastel", dodge=False, legend=False)
plt.title('Emoji Count by Device')
plt.xlabel('Device')
plt.ylabel('Emoji Count')
plt.show()
