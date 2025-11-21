# Fake App Detection CLI

This project is a simple command-line tool that searches the Google Play Store for apps matching a user-provided name and flags potentially fake or impersonating apps based on suspicious keywords and low ratings.

---

## Features
- Searches Play Store using **google_play_scraper**
- Automatically detects **sus keywords** commonly used in fake/malicious apps
- Filters apps based on:
  - Suspicious keywords in title
  - Rating lower than 4.0
- Extracts developer name from the package ID
- Auto-generates an **impersonation report email** for each suspicious app
- Clean CLI output

---

## Requirements
Install required package:

```
pip install google-play-scraper
```

---

## Usage
Run the script:

```
python your_script.py
```

Enter the app name when prompted:

```
Enter the app name: Paytm
```

The script will print:
- All search results
- Suspected fake apps
- Auto-generated email drafts

---

## Detection Logic
The script uses a list of suspicious keywords such as:
- "mods", "hacks", "pro", "vip", "free download", "cracked" etc.

An app is marked suspicious if:
- Its title contains any keyword
- AND its Play Store rating is **below 4.0**

---

## How Impersonation Email Works
Each suspicious app generates:
- A subject line
- A formatted email body

The developer name is extracted from the package ID.
For example:
```
com.facebook.lite  →  facebook
```

---

## Project Structure
```
readme.md
hackathon.py
```

---

## Limitations
- Only checks **Play Store search results** (not APK mirrors)
- Keyword-based detection (simple but effective)
- Doesn't analyze icon similarity, full description text, or developer metadata

---

## Future Improvements
- Add fuzzy title similarity
- Compare icon images using perceptual hashing
- Analyze permissions / SDKs
- Add risk scoring system (0–100)
- Export results to JSON or PDF

---

## Credits
Made for detecting fake apps quickly and generating report emails automatically.



