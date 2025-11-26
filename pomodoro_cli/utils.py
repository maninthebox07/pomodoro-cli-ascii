"""Package-aware utilities.

This version locates package data (sounds) when the project is installed as a package
and falls back to a relative path during development (when running from source).
"""
import os
import time
from pathlib import Path
from pygame import mixer
from importlib import resources


def clear_screen():
    """Clear the terminal screen (cross-platform)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def _get_sound_path():
    """Return a pathlib.Path to the bundled bell.wav.

    First attempt to use importlib.resources.path (works when installed),
    otherwise fall back to the local package directory (useful during dev).
    """
    try:
        # resources.path returns a context manager yielding a pathlib.Path
        with resources.path(__package__, "sounds/bell.wav") as p:
            return p
    except Exception:
        # Fallback: sounds directory relative to this file
        return Path(__file__).parent.joinpath("sounds", "bell.wav")


def play_sound():
    """Play the bell sound using pygame.mixer.

    This function is defensive: if pygame is not available or the file cannot
    be played, it prints an informative message and continues.
    """
    try:
        mixer.init()
        sound_path = _get_sound_path()
        bell = mixer.Sound(str(sound_path))
        bell.play()
        time.sleep(bell.get_length())
    except Exception as e:
        print(f"[Sound disabled. Error: {e}]")