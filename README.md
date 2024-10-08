# Spotify Account Checker (Threaded)

This project is a multi-threaded Spotify account checker using Selenium WebDriver. It validates Spotify account credentials stored in a text file and saves valid accounts in a results folder.

## Features
- Utilizes multi-threading to check multiple accounts simultaneously (up to 5 threads by default).
- Headless browser mode with Chrome WebDriver for faster execution.
- Saves valid accounts in a timestamped results file.
- Color-coded output for easy identification of valid/invalid accounts using `colorama`.

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.x
- Google Chrome browser
- Chromedriver (matching your Chrome version)
- Selenium: `pip install selenium`
- Colorama: `pip install colorama`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/spotify-account-checker.git
   cd spotify-account-checker
## Usage
``` command
python spotify_account_checker.py
