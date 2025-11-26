# API Reference — Pomodoro-CLI

This document lists functions and modules from the project with their signatures, parameters, and return values.

---

## main.py

- main()
  - Description: Start the main application loop and present the menu to the user.
  - Args: None
  - Returns: None (exits the program when the user chooses to leave)

---

## app.py

- timer(total_minutes: int, color: str) -> str
  - Description: Run a blocking countdown timer displaying the remaining time using ASCII art and play a sound when finished. Allows pause via KeyboardInterrupt and provides a small menu while paused.
  - Parameters:
    - total_minutes: Number of minutes to count down from.
    - color: ANSI color code string to render the ASCII time.
  - Returns:
    - 'menu' to indicate the caller should return to the main menu.
    - 'leave' to indicate the caller should close the application.

- ask_for_duration(default: int, string: str) -> int
  - Description: Ask the user whether they want to change the default duration and validate the input.
  - Parameters:
    - default: The default time in minutes.
    - string: A friendly label (e.g., 'Pomodoro', 'Short Break').
  - Returns: The chosen duration in minutes (int). If the user cancels, returns the default.

- ask_to_start(time: int, color: str) -> str
  - Description: Prompt the user to start the timer. If started, runs timer(time, color).
  - Parameters:
    - time: Duration in minutes.
    - color: ANSI color code string for display.
  - Returns:
    - 'menu' to return to the main menu (if user cancels).
    - 'leave' if the timer flow indicates the application should exit.

- run_pomodoro() -> str
  - Description: High-level flow for starting a Pomodoro session (default 25 minutes).
  - Returns: See ask_to_start / timer return values.

- run_short_break() -> str
  - Description: High-level flow for starting a short break (default 5 minutes).
  - Returns: See ask_to_start / timer return values.

- run_long_break() -> str
  - Description: High-level flow for starting a long break (default 15 minutes).
  - Returns: See ask_to_start / timer return values.

---

## utils.py

- clear_screen() -> None
  - Description: Clear the terminal screen for both Windows and POSIX systems.
  - Returns: None

- play_sound() -> None
  - Description: Initialize Pygame mixer and play the bell sound located at `sounds/bell.wav`. If playing fails, prints a diagnostic message but does not raise.
  - Returns: None

---

## ascii_render.py

- title_screen() -> None
  - Description: Print the ASCII title splash to the terminal.
  - Returns: None

- time_finished() -> None
  - Description: Print the ASCII "time finished" message to the terminal.
  - Returns: None

- print_ascii_time(time_str: str, color: str = '') -> None
  - Description: Render a time string (format "MM:SS" or similar) using the ASCII digit definitions.
  - Parameters:
    - time_str: The string containing digits and colon to render.
    - color: Optional ANSI color code applied to the printed lines.
  - Returns: None

---

## ascii_digits.py

- ascii_digits() -> dict
  - Description: Return a dictionary mapping character to a list of 7 strings that visually represent that character in ASCII art.
  - Returns: dict of {char: [7 lines of ASCII art]}

- calculate_max_width(digits: dict) -> int
  - Description: Find the maximum line length among all digits to be used for width-normalization.
  - Returns: Maximum width (int)

- standardize_width(digits: dict, max_width: int) -> dict
  - Description: Pad or trim each line of each digit to be exactly `max_width` characters.
  - Returns: The adjusted digits dictionary.

---

## style.py

- Exports constants for ANSI color codes and formatting:
  - RESET, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BOLD (all strings)

---

Notes
- All user-facing prompts are synchronous and blocking (useful for simple CLI operation).
- Timer uses integer minutes and seconds (the implementation contains a small custom decrement loop — see `timer` docstring).
- Sound playback uses Pygame mixer; failure to play sound does not abort the app.