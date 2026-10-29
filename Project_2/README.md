# Project 2 — Comparative Smartphone Brand Sentiment Analysis

## Overview

This project was completed during a remote data analytics internship with **Brainwave Matrix Solutions** in January 2025. Its goal was to compare sentiment expressed in YouTube comments about **Samsung**, **Google Pixel**, and **Apple iPhone** and investigate which brand received the most favorable reactions in the sampled comments.

The project uses Python scripts to collect top-level YouTube comments and timestamps, clean text, calculate sentiment polarity with TextBlob, and prepare CSV outputs for a Power BI report.

## Tools and technologies

- **Python** — data collection and processing
- **YouTube Data API v3** (`google-api-python-client`) — comment collection
- **Pandas** — CSV and tabular data handling
- **Regular expressions and emoji** — text preprocessing
- **TextBlob** — sentiment polarity scoring
- **Power BI** — report artifact (`.pbix`)

## Repository files

| File | Purpose |
| --- | --- |
| `samsung_with_timestamp.py` | Fetches comments and timestamps for a selected Samsung video |
| `pixel_with_timestamp.py` | Fetches comments and timestamps for a selected Pixel video |
| `iPhone_with_timestamp.py` | Fetches comments and timestamps for a selected iPhone video |
| `cleaning.py` | Removes URLs, emoji, punctuation, and numbers; normalizes comment text |
| `cleaning_2.py` | Parses comment timestamps into a new datetime column |
| `sentiment.py` | Cleans text and computes TextBlob polarity scores; exports per-brand CSV files |
| `Project 2- Sentiment Analysis.pbix` | Power BI report file |

## Workflow

1. **Collect comments:** The three brand-specific scripts use the YouTube Data API to request up to 4,000 top-level comments per selected video, along with publication timestamps.
2. **Clean comments:** `cleaning.py` creates a `Cleaned_Comment` column and saves cleaned CSVs.
3. **Process timestamps:** `cleaning_2.py` converts the `Timestamp` field into `Timestamps_Cleaned`.
4. **Calculate sentiment:** `sentiment.py` uses `TextBlob(...).sentiment.polarity` and writes a `Sentiment` score for each comment.
5. **Visualize:** The repository includes a Power BI report associated with the analysis. Its internal visuals and data-source configuration have not been independently verified here.

### Understanding polarity

TextBlob polarity ranges from **-1** (negative) to **+1** (positive), with **0** representing neutral polarity. The script produces numerical polarity scores rather than a separately validated sentiment classification model.

## Reproducing the original approach

The scripts use `pandas`, `google-api-python-client`, `emoji`, and `textblob`. They require a configured YouTube Data API key and access to the selected videos.

**Important:** The original scripts are archived as submitted, and the pipeline is **not directly reproducible without adjustments**. In particular, the Samsung collection script writes `YouTube_Comments_with_Timestamps.csv`, while subsequent scripts expect Samsung-specific filenames. Some cleaning stages also expect different intermediate filenames. Run scripts from the `Project_2` folder and reconcile filenames before attempting a full rerun. The report may also require updated CSV source paths.

The original collection scripts contain a **hardcoded API key**. Revoke or rotate any active key before reuse; removing it from current files alone does not remove it from Git history. Never commit a replacement key.

## Scope and limitations

- Comments were sampled from selected YouTube videos, not from all smartphone users.
- Video audiences and discussion context can affect comparisons between brands.
- TextBlob polarity is a lexicon-based estimate and may misinterpret sarcasm, slang, or mixed opinions.
- The repository does not include a manually labeled evaluation dataset or documented accuracy metrics.
- The code reflects an early internship learning project rather than a production-ready pipeline.

## Learning outcomes

This project provided hands-on practice with API-based data collection, CSV processing, text cleaning, introductory NLP sentiment analysis, and preparing results for dashboard reporting.
