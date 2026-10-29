"""Clean collected YouTube comments for the three smartphone brands."""
import re
import emoji
import pandas as pd

BRANDS = ("Samsung", "Pixel", "iPhone")


def clean_text(value: object) -> str:
    if pd.isna(value):
        return ""
    text = str(value)
    text = re.sub(r"https?://\\S+|www\\.\\S+", "", text)
    text = "".join(char for char in text if char not in emoji.EMOJI_DATA)
    text = re.sub(r"[^A-Za-z\\s]", "", text)
    return re.sub(r"\\s+", " ", text).strip().lower()


def main() -> None:
    for brand in BRANDS:
        source = f"YouTube_{brand}_Comments_with_Timestamps.csv"
        frame = pd.read_csv(source)
        if "Comment" not in frame.columns:
            raise ValueError(f"{source} is missing the Comment column")
        frame["Cleaned_Comment"] = frame["Comment"].apply(clean_text)
        output = f"Cleaned_{source}"
        frame.to_csv(output, index=False)
        print(f"Saved {output}")


if __name__ == "__main__":
    main()
