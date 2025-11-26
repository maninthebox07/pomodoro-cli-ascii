"""Entrypoint for the pomodoro-cli package.

This module provides the console entrypoint `pomodoro-cli` (configured in pyproject.toml).
It mirrors the behavior of the original top-level main.py but uses package-relative imports.
"""
from time import sleep
from .utils import clear_screen
from .ascii_render import title_screen
from .app import run_pomodoro, run_short_break, run_long_break
from .style import RED, GREEN, RESET


def main():
    """Main menu loop.

    Use as console entrypoint: `pomodoro-cli` (after installation) or:
      python -m pomodoro_cli.main
    """
    while True:
        clear_screen()
        title_screen()
        print(f'[{GREEN}1{RESET}] Pomodoro\n[{GREEN}2{RESET}] Short Break\n[{GREEN}3{RESET}] Long Break\n[{RED}4{RESET}] Leave')

        try:
            option = input('\nSelect the option (1, 2, 3 or 4): ').strip()

            match option:
                case '1':
                    clear_screen()
                    result = run_pomodoro()
                    if result == 'leave':
                        print('\nLeaving...')
                        sleep(1)
                        break
                case '2':
                    clear_screen()
                    result = run_short_break()
                    if result == 'leave':
                        print('\nLeaving...')
                        sleep(1)
                        break
                case '3':
                    clear_screen()
                    result = run_long_break()
                    if result == 'leave':
                        print('\nLeaving...')
                        sleep(1)
                        break
                case '4':
                    print('Leaving...')
                    sleep(1)
                    break
                case _:
                    print('Invalid option. Please, enter a number between 1 and 4.')
                    sleep(2.5)
        except KeyboardInterrupt:
            # Allow user to leave with Ctrl+C from the menu
            print('\n\nLeaving...')
            sleep(1)
            break


if __name__ == "__main__":
    main()