<p align="center"> <img src="assets/banner.png" alt="Pomodoro banner" width="800" /> </p>

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
1. Copy the repository files (the app is a small set of .py files).
2. (Optional) Install dependencies for sound:
   pip install pygame
3. Make sure the sound file exists:
   - Place a `bell.wav` file at `./sounds/bell.wav` relative to the project root (same folder containing the .py files).
4. Run:
   python main.py

Installation (recommended)
- Create and activate a virtual environment (optional but recommended):
  python -m venv .venv
  source .venv/bin/activate     # Linux / macOS
  .venv\Scripts\activate        # Windows
- Install Pygame (for sound):
  pip install pygame

Usage
- Start the app:
  python main.py
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

Project structure
- main.py — entrypoint and CLI menu
- app.py — core pomodoro logic and timer flow
- utils.py — helper functions (clear screen, play sound)
- ascii_render.py — title and large ASCII time rendering
- ascii_digits.py — ASCII digits source and helpers
- style.py — ANSI color constants
- sounds/bell.wav — expected sound file (not included in this code bundle)

Contributing
- Bug reports, suggestions, and PRs are welcome.
- Keep changes small and document any behavior changes.
- Follow Python conventions and keep compatibility with Python 3.10+.

License
- Add your preferred license here (e.g., MIT) or remove this section if not needed.
```