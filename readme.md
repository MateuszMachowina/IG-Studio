# ✦ IG Studio 2026

A unified desktop application for downloading, viewing, exporting, and tracking your Instagram data - all running locally on your machine, no third-party services involved.

**Key advantage:** The application uses your active session ID directly to communicate with Instagram. It never asks for your password.

---

## 📦 Requirements

| Tool | Why it's needed |
|------|----------------|
| **Python 3.11+** | Runtime for the application |
| **FFmpeg** | Video processing and thumbnail extraction — add to Windows PATH |
| **VLC Media Player** | Video playback in the viewer — must be 64-bit, matching Python |

### Install Python dependencies

```bash
pip install -r requirements.txt
```
*(Dependencies include `requests`, `pillow`, `python-vlc`)*

---

## 🚀 How to Run

Simply launch the main dashboard:
```bash
python main.py
```
This will open the **Instagram Studio 2026** graphical interface, where you can navigate between all the tools using the left sidebar.

### Providing your Session ID
The first time you use the Downloader or Tracker, you will be prompted to paste your **Session ID**. 
You can get this from your browser's developer tools (F12) -> Application / Storage -> Cookies -> `sessionid`.
For convenience across tabs, this is saved locally in an `app_config.json` file.

---

## 🛠️ The Tools

### 1. 📥 Downloader (Highlights)
Downloads all highlights from any Instagram account.
- Supports multiple accounts — each saved to its own subfolder (`highlights/username/`)
- Downloads original quality MP4s and JPEGs
- Skips already-downloaded files on re-run — safe to sync repeatedly
- Saves metadata for the Viewer and Exporter

### 2. 👥 Follow Tracker
Tracks changes in your follower/following lists over time.
- Compares current state against the previously saved state
- Generates a readable report showing:
  - 💔 **Unfollowers** (people who stopped following you)
  - 🎉 **New followers** 
  - 🔍 **Non-followers** (people you follow who don't follow back)
- Built-in delay to prevent rate-limiting

### 3. 👁️ Story Viewer
A local player that plays your downloaded highlights with an Instagram-style interface.
- Sidebar with gradient avatar rings and supersampled thumbnails
- Story progress bars at the top of the player
- Tap left/right half of the video to go prev/next
- VLC-powered video playback with original audio

### 4. 🎬 MP4 Exporter
Converts downloaded highlight collections into single vertical MP4 files.
- **1080×1920** output (Instagram story resolution)
- Bakes in an Instagram-style overlay (gradient scrim, progress bars, avatar ring, collection title)
- Crossfade transitions between clips
- Original audio preserved

---

## 🗂️ Folder Structure

```text
project/
├── main.py                      ← main GUI entrypoint
├── src/                         ← application source code
│   ├── downloader.py
│   ├── tracker.py
│   ├── viewer.py
│   ├── exporter.py
│   └── config.py
│
├── app_config.json              ← (auto-generated) holds your session_id
├── highlights/                  ← created by downloader
├── exports/                     ← created by exporter
├── flags/                       ← cached flags for the viewer
└── unfollowers_data/            ← saved by tracker
```

---

## 🔒 Security & Privacy

This application runs entirely on your local machine. It never sends your data to any external server. It only communicates directly with Instagram using your session token.

**Never commit your personal data to version control.** If you upload this project to GitHub, ensure that `.gitignore` is set up properly or manually exclude the `app_config.json` file and all data folders (`highlights/`, `exports/`, `unfollowers_data/`).

---

## ⚠️ Troubleshooting & Legal Disclaimer

- **Error 429:** Instagram temporarily blocked requests from your IP. Wait 15–30 minutes before trying again.
- **VLC black screen / not working:** Ensure you have the **64-bit** version of VLC installed, matching your 64-bit Python installation.
- **FFmpeg not found:** Download FFmpeg, extract it, and add the `bin/` folder to your Windows PATH.

*This project is for personal, educational use only. It is not affiliated with Meta Platforms, Inc. or Instagram in any way. Use it responsibly to avoid rate limits.*
