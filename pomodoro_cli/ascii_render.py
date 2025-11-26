'''ascii digits rendering functions

High-level rendering helpers that use the digit definitions in ascii_digits.py
to print a large, stylized time and other screens.
'''
from .ascii_digits import ascii_digits, calculate_max_width, standardize_width
from .style import GREEN, RED, BOLD, RESET


def title_screen():
    """Print the application's ASCII title splash screen."""
    print(RED + '''
                                       __                                   ___           
                                      /\\ \\                                 /\\_ \\    __    
 _____     ___     ___ ___     ___    \\_\\ \\    ___   _ __   ___         ___\\//\\ \\  /\\_\\   
/\\ '__`\\  / __`\\ \\/' __` __`\\ / __`\\  /'_` \\  / __`\\/\\`'__\\/ __`\\      /'___\\\\ \\ \\ \\/\\ \\  
\\ \\ \\L\\ \\/\\ \\L\\ \\/\\ \\/\\ \\/\\ \\/\\ \\L\\ \\/\\ \\L\\ \\/\\ \\L\\ \\ \\ \\//\\ \\L\\ \\    /\\ \\__/ \\_\\ \\_\\ \\ \\ 
 \\ \\ ,__/\\ \\____/\\ \\_\\ \\_\\ \\_\\ \\____/\\ \\___,_\\ \\____/\\ \\_\\\\ \\____/    \\ \\____\\/\\____\\\\ \\_\\
  \\ \\ \\/  \\/___/  \\/_/\\/_/\\/_/\\/___/  \\/__,_ /\\/___/  \\/_/ \\/___/      \\/____/\\/____/ \\/_/
   \\ \\_\\                                                                                  
    \\/_/                                                                                  
''' + RESET)


def time_finished():
    """Print a completion ASCII message when the timer finishes."""
    print(GREEN + '''
 __                                   ___                          __                 __  __     
/\\ \\__  __                          /'___\\ __          __         /\\ \\               /\\ \\/\\ \\    
\\ \\ ,_\\/\\_\\    ___ ___      __     /\\ \\__//\\_\\    ___ /\\_\\    ____\\ \\ \\___      __   \\_\\ \\ \\ \\   
 \\ \\ \\/\\/\\ \\ /' __` __`\\  /'__`\\   \\ \\ ,__\\/\\ \\ /' _ `\\/\\ \\  /',__\\\\ \\  _ `\\  /'__`\\/\\'_` \\ \\ \\  
  \\ \\ \\_\\ \\ \\/\\ \\/\\ \\/\\ \\/\\  __/    \\ \\ \\_/\\ \\ \\/\\ \\/\\ \\ \\ \\/\\__, `\\\\ \\ \\ \\ \\/\\  __//\\ \\L\\ \\ \\_\\ 
   \\ \\__\\\\ \\_\\ \\_\\ \\_\\ \\_\\ \\____\\    \\ \\_\\  \\ \\_\\ \\_\\ \\_\\ \\_\\/\\____/ \\ \\_\\ \\_\\ \\____\\ \\___,_\\/\\_\\
    \\/__/ \\/_/\\/_/\\/_/\\/_/\\/____/     \\/_/   \\/_/\\/_/\\/_/\\/_/\\/___/   \\/_/\\/_/\\/____/ \\/__,_ /\\/_/                                                                                
    ''' + RESET)


def print_ascii_time(time_str, color=''):
    """Render an ASCII-art representation of the given time string.

    Args:
        time_str (str): String containing digits and colon, e.g. "25:00".
        color (str): ANSI color code to apply to the printed ASCII lines.
    """
    digits = ascii_digits()
    max_width = calculate_max_width(digits)

    # Ensure all digit art has the same width
    digits = standardize_width(digits, max_width)

    # Each digit drawing is 7 lines tall; compose lines horizontally
    for line_index in range(7):
        final_line = ''
        for char in time_str:
            # Concatenate the corresponding line of each character
            final_line += digits[char][line_index]
        print(color + final_line + RESET)