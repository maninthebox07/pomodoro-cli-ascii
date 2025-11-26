``` 
 ███████████     ███████    ██████   ██████    ███████    ██████████      ███████    ███████████      ███████   
░░███░░░░░███  ███░░░░░███ ░░██████ ██████   ███░░░░░███ ░░███░░░░███   ███░░░░░███ ░░███░░░░░███   ███░░░░░███ 
 ░███    ░███ ███     ░░███ ░███░█████░███  ███     ░░███ ░███   ░░███ ███     ░░███ ░███    ░███  ███     ░░███
 ░██████████ ░███      ░███ ░███░░███ ░███ ░███      ░███ ░███    ░███░███      ░███ ░██████████  ░███      ░███
 ░███░░░░░░  ░███      ░███ ░███ ░░░  ░███ ░███      ░███ ░███    ░███░███      ░███ ░███░░░░░███ ░███      ░███
 ░███        ░░███     ███  ░███      ░███ ░░███     ███  ░███    ███ ░░███     ███  ░███    ░███ ░░███     ███ 
 █████        ░░░███████░   █████     █████ ░░░███████░   ██████████   ░░░███████░   █████   █████ ░░░███████░  
░░░░░           ░░░░░░░    ░░░░░     ░░░░░    ░░░░░░░    ░░░░░░░░░░      ░░░░░░░    ░░░░░   ░░░░░    ░░░░░░░    

<p align="center"><strong>Pomodoro</strong> — a lightweight terminal Pomodoro timer (Python 3.10+, Pygame optional).</p>

# Pomodoro-CLI

A lightweight command-line Pomodoro timer written in Python using ASCII art for a big timer display and optional sound notification via Pygame.

Features
- Simple CLI menu with Pomodoro, Short Break, and Long Break modes.
- ASCII-art time rendering for a large, visual countdown.
- Configurable durations at runtime.
- Pause/resume, return to menu, or exit during a running timer.
- Optional sound notification when the timer finishes (requires Pygame and a `sounds/bell.wav` file).

Requirements
- Python 3.10 or newer
- Pygame (for sound playback) — optional but recommended

Quick start (local)
1. Clone or copy the repository files (the app is a small set of .py files).
2. (Optional) Install dependencies for sound:
   pip install pygame
3. Make sure the sound file exists:
   - Place a `bell.wav` file at `./pomodoro_cli/sounds/bell.wav` relative to the package root.
4. Run:
   python -m pomodoro_cli.main
   or, after installing the package:
   pomodoro-cli

Installation (recommended)
- Create and activate a virtual environment (optional but recommended):
  python -m venv .venv
  source .venv/bin/activate     # Linux / macOS (use .venv/bin/activate.fish for fish)
  .venv\Scripts\activate        # Windows
- Install Pygame (for sound, optional):
  pip install pygame

Usage
- Start the app:
  python -m pomodoro_cli.main
  or (after install)
  pomodoro-cli
- Menu options:
  1 — Pomodoro (default 25 minutes)
  2 — Short Break (default 5 minutes)
  3 — Long Break (default 15 minutes)
  4 — Leave
- When choosing Pomodoro / Break:
  - You'll be asked whether to change the default time (in minutes).
  - Confirm start (`Y` or Enter) to begin the countdown.
  - During a running timer press Ctrl+C to pause; you can then:
    1 — Resume timer
    2 — Return to menu
    3 — Leave the app

Notes & troubleshooting
- If Pygame is not installed or the sound file is missing, the app will continue to work but will print a sound-related error message. Sound is optional.
- The ASCII display depends on terminal width. If the timer output appears misaligned, try enlarging the terminal window.
- For accessibility, a short plain-text title is provided below the banner so screen readers can identify the project.

Project structure
- pomodoro_cli/
  - __init__.py
  - main.py
  - app.py
  - utils.py
  - ascii_render.py
  - ascii_digits.py
  - style.py
  - sounds/
    - bell.wav (expected)
- README.md
- pyproject.toml
- MANIFEST.in
- LICENSE
- .github/

Contributing
- Bug reports, suggestions, and PRs are welcome.
- Keep changes small and document any behavior changes.
- Follow Python conventions and keep compatibility with Python 3.10+.

License
- MIT (see LICENSE file in this repository)
```