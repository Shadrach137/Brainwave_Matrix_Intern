#Import relevant libraries
import pandas as pd
import re
import emoji

# Function to clean comments
def clean_text(text):
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    # Remove emoji
    text = ''.join([c for c in text if c not in emoji.EMOJI_DATA])
    # Remove special characters, numbers, and punctuation
    text = re.sub(r"[^A-Za-z\s]", "", text)
    # Convert to lowercase
    text = text.lower()
    return text

# List of CSV files to clean
csv_files = [
    "YouTube_Comments_with_Timestamps.csv",
    "YouTube_Pixel_Comments_with_Timestamps.csv",
    "YouTube_iPhone_Comments_with_Timestamps.csv"
]

# Process each CSV file
for file in csv_files:
    # Load the CSV file
    df = pd.read_csv(file)

    # Check if 'Comment' column exists in the CSV
    if 'Comment' in df.columns:
        # Clean the 'Comment' column
        df['Cleaned_Comment'] = df['Comment'].apply(clean_text)

        # Save the cleaned data back to a new CSV file
        cleaned_file = f"Cleaned_{file}"
        df.to_csv(cleaned_file, index=False)
        print(f"Cleaned comments saved to {cleaned_file}")
    else:
        print(f"The 'Comment' column was not found in {file}.")

