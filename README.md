# Simple Web Opener

## Description
Simple Web Opener is a Python-based command-line tool that allows users to quickly open websites by entering URLs directly in the terminal. It ensures efficiency by automatically adding missing protocols, validating URLs, and maintaining a search history.

## Features
- Open multiple websites at once (comma or space-separated input)
- Automatically adds "https://" if missing from URLs
- Validates URLs before opening them in the browser
- Saves visited websites in a search history file
- View previously visited websites
- Open all previously visited websites
- Clear search history
- Interactive mode that continuously accepts user input until "exit" is entered

## Installation
1. Clone this repository or download the script.
2. Ensure Python is installed (Python 3 recommended).
3. Install dependencies:
   pip install validators;

## Usage
Run the script in the terminal:
    python script.py;

### Available Commands:
- Enter a URL (or multiple URLs separated by space or comma) to open it in the default web browser.
- `history` - View the search history.
- `clear history` - Delete the search history.
- `open all` - Open all URLs stored in the search history.
- `exit` - Exit the program.

## How It Works
1. The program prompts the user for a website URL.
2. It validates and formats the URL correctly (adds "https://" if missing).
3. If valid, the URL is opened in the default web browser.
4. The URL is saved in a history file (`search_history.txt`) to avoid duplication.
5. The user can interactively manage the search history and continue entering URLs.

## Example Usage
```sh
Enter a website (or 'exit', 'history', 'clear history', 'open all'): google.com
Opening: https://google.com
 URL saved: https://google.com

Enter a website (or 'exit', 'history', 'clear history', 'open all'): history
1. 2025-03-12 14:30:45 - https://google.com

Enter a website (or 'exit', 'history', 'clear history', 'open all'): open all
Opening: https://google.com
```

## License
This project is open-source and available under the MIT License.

