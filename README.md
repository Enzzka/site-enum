# site-enum

My very first script. The code is probably messy and far from perfect, but it works. Just logging my progress.

A simple web directory and sensitive file scanner using Python's native socket and SSL libraries to detect common hidden paths (like admin panels, configs, and backups).

## Feedback & Critics

Any critics, suggestions, or advice are highly welcome! Feel free to open an issue or leave a comment if you have tips on how I can optimize this script or clean up the code.

##  Requirements

- Python 3.x
- No external libraries required (uses built-in `socket` and `ssl` modules).

##  How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Enzzka/site-enum.git
   ```

2. Open the script and change the `domain` variable to your target website (default is `www.google.com`).

3. Run the script via terminal:
   ```bash
   python site-enum.py
   ```
