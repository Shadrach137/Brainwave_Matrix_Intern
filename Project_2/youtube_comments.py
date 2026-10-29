"""Collect top-level YouTube comments and publication timestamps."""
import os
import pandas as pd
from googleapiclient.discovery import build


def fetch_comments(video_id: str, max_comments: int = 4000) -> list[dict]:
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise RuntimeError("Set YOUTUBE_API_KEY in your environment before running.")
    youtube = build("youtube", "v3", developerKey=api_key)
    comments = []
    page_token = None
    while len(comments) < max_comments:
        response = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=page_token,
            maxResults=min(100, max_comments - len(comments)),
            textFormat="plainText",
        ).execute()
        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "Comment": snippet["textDisplay"],
                "Timestamp": snippet["publishedAt"],
            })
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return comments


def save_comments(video_id: str, output_file: str, max_comments: int = 4000) -> None:
    comments = fetch_comments(video_id, max_comments)
    pd.DataFrame(comments, columns=["Comment", "Timestamp"]).to_csv(output_file, index=False)
    print(f"Saved {len(comments)} comments to {output_file}")
