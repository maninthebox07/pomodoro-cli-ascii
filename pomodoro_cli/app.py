'''main pomodoro app functions

Contains the timer loop and user interaction logic for starting and
configuring Pomodoro and break timers.
'''
from time import sleep
from utils import clear_screen, play_sound
from ascii_render import print_ascii_time, time_finished
from style import YELLOW, BLUE, CYAN, GREEN, RED, MAGENTA, RESET


def timer(total_minutes, color):
    """Run the countdown timer.

    The function renders the current minutes and seconds using ASCII art
    and sleeps 1 second between updates. The countdown is driven in a
    custom way: seconds are decremented until they reach zero; when both
    minutes and seconds are zero, the timer ends.

    Args:
        total_minutes (int): Number of minutes to count down from.
        color (str): ANSI color code used to render the ASCII time.

    Returns:
        str: 'menu' to instruct caller to return to the main menu,
             'leave' to indicate the application should exit.
    """
    minutes = total_minutes
    seconds = 0

    while True:
        try:
            clear_screen()
            print_ascii_time(f"{minutes:02d}:{seconds:02d}", color)
            sleep(1)

            if seconds == 0:
                if minutes == 0:
                    break
                minutes -= 1
                seconds = 59
            else:
                seconds -= 1

        except KeyboardInterrupt:
            # Pause handling: while paused, present options to user.
            clear_screen()
            while True:
                print('\n\nTimer paused!')
                print(f'[{GREEN}1{RESET}] Resume Timer\n[{GREEN}2{RESET}] Return to menu\n[{RED}3{RESET}] Leave')

                choice = input('\nChoose: ').strip()

                match choice:
                    case '1':
                        # Resume timer by breaking out of the pause loop.
                        break
                    case '2':
                        # Indicate to caller that user wants to return to menu.
                        return 'menu'
                    case '3':
                        # Indicate to caller that user wants to exit the app.
                        return 'leave'
                    case _:
                        print('\nInvalid option. Please, enter a number between 1 and 3.\n')

    # When timer finishes:
    clear_screen()
    time_finished()
    # Play sound (non-fatal if it fails).
    play_sound()
    input('Press ENTER to return to the menu...')

    return 'menu'


def ask_for_duration(default, string):
    """Ask the user whether they want to change a default duration.

    The function prompts to change the default value and validates
    the provided input ensuring it is an integer greater than zero.

    Args:
        default (int): Default time in minutes.
        string (str): Human-friendly label (e.g., 'Pomodoro', 'Short Break').

    Returns:
        int: The chosen duration in minutes (or `default` if user cancels).
    """
    change = input(f'Change {string} time (minutes)? [y/N]: ').strip().lower()

    if change == 'n' or change == '':
        return default

    while True:
        new_time = input("Set time (minutes) [ENTER to cancel]: ").strip()

        if new_time == '':
            # User cancelled input -> keep default
            return default

        try:
            value = int(new_time)
            if value <= 0:
                print("Enter a number greater than zero.\n")
                continue
            return value
        except ValueError:
            print('Enter a valid number.\n')


def ask_to_start(time, color):
    """Prompt the user to start the timer.

    Accepts 'Y' or Enter to start; 'n' to cancel and return to menu.

    Args:
        time (int): Duration in minutes.
        color (str): ANSI color code to use when rendering time.

    Returns:
        str: The result returned by `timer` or 'menu' if user cancels.
    """
    while True:
        start = input('Start? [Y/n]').strip()

        if start.upper() == 'Y' or start == '':
            return timer(time, color)
        elif start.lower() == 'n':
            return 'menu'
        else:
            print('Invalid option. Try again.\n')


def run_pomodoro():
    """Start the Pomodoro flow (default 25 minutes).

    Returns:
        str: The navigation result from `ask_to_start`.
    """
    time = ask_for_duration(25, 'Pomodoro')

    result = ask_to_start(time, MAGENTA)
    return result


def run_short_break():
    """Start the short break flow (default 5 minutes).

    Returns:
        str: The navigation result from `ask_to_start`.
    """
    time = ask_for_duration(5, 'Short Break')

    result = ask_to_start(time, CYAN)
    return result


def run_long_break():
    """Start the long break flow (default 15 minutes).

    Returns:
        str: The navigation result from `ask_to_start`.
    """
    time = ask_for_duration(15, 'Long Break')

    result = ask_to_start(time, BLUE)
    return result