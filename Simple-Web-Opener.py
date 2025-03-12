# Simple Web Opener -> Powered by Romaniuc Albert-Iulian

# Description:
# This program allows users to quickly open websites by entering URLs directly in the terminal.
# It automatically adds "https://" if missing, validates the URLs, and stores them in a history file.
# Users can:
#   - Open multiple websites at once (comma or space separated)
#   - View their search history
#   - Open all previously searched websites
#   - Clear the search history
# The program is interactive and continuously accepts input until the user types "exit".

import webbrowser
import validators
import os
from datetime import datetime

HISTORY_FILE = "search_history.txt"  # File where search history is stored

# ========================
# Function to save URLs to history
# This function ensures URLs are not duplicated in the history file
# ========================
def save_history(url):
    """Saves the URL in the history file, avoiding duplicates."""
    history = set()
    
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = {line.strip().split(" - ")[-1] for line in f if " - " in line}

    if url not in history:
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {url}\n")
        print(f" URL saved: {url}")
    else:
        print(f" URL already exists in history.")

# ========================
# Function to load and display search history
# Reads the history file and prints all previously searched URLs
# ========================
def load_history():
    """Displays the search history from the file."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = f.readlines()
        if history:
            print("\n Search History:")
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry.strip()}")
        else:
            print(" History is empty.")
    else:
        print(" No search history found.")

# ========================
# Function to clear search history
# Deletes the history file if it exists
# ========================
def clear_history():
    """Deletes the search history file."""
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)
        print(" Search history cleared.")
    else:
        print(" No search history found.")

# ========================
# Function to open websites
# Takes user input, validates the URLs, opens them in a browser, and saves them to history
# ========================
def open_website():
    """Asks for URLs, validates them, opens them in the browser, and saves them to history."""
    while True:
        user_input = input("\n🔍 Enter a website (or 'exit', 'history', 'clear history', 'open all'): ").strip().lower()

        if user_input == 'exit':
            print(" Exiting program.")
            break
        elif user_input == 'history':
            load_history()
            continue
        elif user_input == 'clear history':
            clear_history()
            continue
        elif user_input == 'open all':
            if os.path.exists(HISTORY_FILE):
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    urls = [line.strip().split(" - ")[-1] for line in f if " - " in line]
                
                if not urls:
                    print("📂 No URLs found in history.")
                else:
                    print(" Opening all saved websites...")
                    for url in urls:
                        webbrowser.open(url)
                        print(f" Opening: {url}")
            else:
                print(" No search history found.")
            continue

        # Allow multiple URLs separated by space or comma
        urls = [url.strip() for url in user_input.replace(",", " ").split()]
        for url in urls:
            if not url.startswith(("http://", "https://")):
                url = "https://" + url
            if not validators.url(url):
                print(f" Invalid URL: {url}. Skipping.")
                continue
            webbrowser.open(url)
            print(f" Opening: {url}")
            save_history(url)

# ========================
# Main program execution
# Calls the open_website function to start the program
# ========================
if __name__ == "__main__":
    open_website()
