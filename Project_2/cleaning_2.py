#Import relevant libraries
import pandas as pd

# Load the respective CSV files
df_samsung = pd.read_csv('Cleaned_YouTube_Samsung_Comments_with_Timestamps.csv')
df_pixel = pd.read_csv('Cleaned_YouTube_Pixel_Comments_with_Timestamps.csv')
df_iphone = pd.read_csv('Cleaned_YouTube_iPhone_Comments_with_Timestamps.csv')

# Convert 'Timestamp' to datetime and store it in a new column 'Timestamps_Cleaned'
if 'Timestamp' in df_samsung.columns:
    df_samsung['Timestamps_Cleaned'] = pd.to_datetime(df_samsung['Timestamp'])

if 'Timestamp' in df_pixel.columns:
    df_pixel['Timestamps_Cleaned'] = pd.to_datetime(df_pixel['Timestamp'])

if 'Timestamp' in df_iphone.columns:
    df_iphone['Timestamps_Cleaned'] = pd.to_datetime(df_iphone['Timestamp'])

# Save the modified DataFrames to new CSV files
df_samsung.to_csv('YouTube_Samsung_Comments_with_Cleaned_Timestamps.csv', index=False)
df_pixel.to_csv('YouTube_Pixel_Comments_with_Cleaned_Timestamps.csv', index=False)
df_iphone.to_csv('YouTube_iPhone_Comments_with_Cleaned_Timestamps.csv', index=False)

print("Created 'Timestamps_Cleaned' column and saved to new CSV files.")
