"""Package-aware utilities.

This module provides cross-platform functionality for clearing the screen
and playing the Pomodoro bell sound, ensuring compatibility whether the
project is run from source or installed as a package.
"""
import os
import time
from pathlib import Path
from importlib import resources

# 1. Attempt to import pygame.mixer and set a global flag.
# This makes sound functionality optional if pygame isn't installed.
try:
    from pygame import mixer
    HAS_SOUND_SUPPORT = True
except ImportError:
    mixer = None 
    HAS_SOUND_SUPPORT = False
    print("[WARN] The 'pygame' module was not found. Sound features are disabled.")


def clear_screen():
    """Clear the terminal screen (cross-platform)."""
    # Uses 'cls' for Windows (nt) and 'clear' for Unix/Linux/macOS.
    os.system('cls' if os.name == 'nt' else 'clear')


def _get_sound_path():
    """Returns a pathlib.Path object pointing to the bundled 'bell.wav'.

    This function is crucial for finding the sound file correctly:
    1. Tries to locate it using importlib.resources (for installed packages).
    2. Falls back to a relative path using Path(__file__).parent (for development/run-from-source).

    Returns:
        pathlib.Path: The absolute path to the bell.wav file.
    """
    # Assuming the module is part of a package (e.g., 'pomodoro_cli')
    # and the sound is in a submodule 'sounds'.
    try:
        # Use importlib.resources.path for robust package data access
        with resources.path(__package__, "sounds/bell.wav") as p:
            return p
    except Exception:
        # Fallback for when running directly from the source directory
        return Path(__file__).parent.joinpath("sounds", "bell.wav")


def play_sound():
    """Play the bell sound using pygame.mixer.

    This function checks if sound support is available first. If available,
    it initializes the mixer, loads the sound file (using the package-aware path),
    plays it, and blocks execution until the sound finishes.
    """
    # Skip execution if pygame failed to import.
    if not HAS_SOUND_SUPPORT:
        print("[Sound disabled]")
        return
        
    try:
        # Initialize the mixer and load the sound file path.
        mixer.init()
        sound_path = _get_sound_path()
        bell = mixer.Sound(str(sound_path))
        
        # Play and wait for the sound to finish.
        bell.play()
        time.sleep(bell.get_length())
        
    except Exception as e:
        # Catch exceptions like: file not found (if fallback fails), 
        # or error initializing audio devices.
        print(f"[Sound disabled. Error: {e}]")