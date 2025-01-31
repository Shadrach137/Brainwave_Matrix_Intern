import googleapiclient.discovery
import pandas as pd

# Set up the YouTube API client
api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyBcv8XyL8AC2WBKBlGtIBgNBgTfg9p6SWc"  # Replace with your own API key

# Initialize YouTube API client
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

def fetch_comments(video_id, max_comments=4000):
    comments = []
    next_page_token = None
    fetched_count = 0  # Counter for fetched comments

    while next_page_token != "end" and fetched_count < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=100  # Fetch 100 comments per request
        )
        response = request.execute()

        for item in response["items"]:
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comment_timestamp = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
            comments.append({"Comment": comment_text, "Timestamp": comment_timestamp})
            fetched_count += 1

            # Stop fetching if we reach the max_comments limit
            if fetched_count >= max_comments:
                next_page_token = "end"
                break

        # Get the next page token
        next_page_token = response.get("nextPageToken", "end")

        # Stop fetching if there are no more comments
        if next_page_token == "end":
            break

    return comments

# Example usage
video_id = "63EVXf_S4WQ"  # Replace with the actual video ID
comments = fetch_comments(video_id)
print(f"Fetched {len(comments)} comments")

# Save to a CSV
df = pd.DataFrame(comments)
df.to_csv("YouTube_Pixel_Comments_with_Timestamps.csv", index=False)
print("Comments saved to YouTube_Pixel_Comments_with_Timestamps.csv")
