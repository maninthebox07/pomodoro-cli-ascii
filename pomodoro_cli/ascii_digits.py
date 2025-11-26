'''ascii digits handling functions

Provides the ASCII art digit definitions and helper utilities to normalize
their widths for consistent rendering.
'''


def ascii_digits():
    """Return the ASCII representation dictionary for digits and colon.

    Each character maps to a list of 7 strings (one for each line of the
    ASCII-art digit).
    """
    digits_dictionary = {
        "0": [
            "   __",
            " /'__`\\ ",
            "/\\ \\/\\ \\ ",
            "\\ \\ \\ \\ \\ ",
            " \\ \\ \\_\\ \\ ",
            "  \\ \\____/",
            "   \\/___/"
        ],
        "1": [
            "   _",
            " /' \\",    
            "/\\_, \\",   
            "\\/_/\\ \\",  
            "   \\ \\ \\",
            "    \\ \\_\\",
            "     \\/_/"
        ],
        "2": [
            "  ___",
            "/'___`\\",
            "/\\_\\ /\\ \\",
            "\\/_/// /__",
            "   // /_\\ \\",
            "   /\\______/",
            "   \\/_____/"
        ],
        "3": [
            "   __",
            " /'__`\\",
            "/\\_\\\\L\\ \\",
            "\\/_/_\\_<_",
            "  /\\ \\L\\ \\",
            "  \\ \\____/",
            "   \\/___/"
        ],
        "4": [
            " __ __",
            "/\\ \\\\ \\",
            "\\ \\ \\\\ \\",
            " \\ \\ \\\\ \\_",
            "  \\ \\__ ,__\\",
            "   \\/_/\\_\\_/",
            "        \\/_/"
        ],
        "5": [
            " ______",
            "/\\  ___\\",
            "\\ \\ \\__/",
            " \\ \\___``\\",
            "  \\/\\ \\L\\ \\",
            "   \\ \\____/",
            "    \\/___/"
        ],
        "6": [
            "  ____",
            " /'___\\",   
            "/\\ \\__/", 
            "\\ \\  _``\\",
            " \\ \\ \\L\\ \\",
            "  \\ \\____/",
            "   \\/___/"
        ],
        "7": [
            " ________ ",
            "/\\_____  \\",
            "\\/___//'/'",
            "    /' /'",
            "   /' /'",
            "  /\\_/",
            "  \\//"
        ],
        "8": [
            "   __",
            " /'_ `\\",
            "/\\ \\L\\ \\",
            "\\/_> _ <_",
            " /\\ \\L\\ \\",
            " \\ \\____/",
            "   \\/___/"
        ],
        "9": [
            "   __",
            " /'_ `\\",
            "/\\ \\L\\ \\",
            "\\ \\___, \\",
            "\\ /__,/\\ \\",
            "      \\ \\_\\",
            "       \\/_/"
        ],
        ":": [
            "   __",
            "  /\\_\\",
            "  \\/_/_",
            "    /\\_\\",
            "    \\/_/",
            "       ",
            "       "
        ]
    }

    return digits_dictionary


def calculate_max_width(digits):
    """Calculate the maximum line width among all digits.

    Args:
        digits (dict): Dictionary returned by `ascii_digits()`.

    Returns:
        int: Maximum length (in characters) of any line in the digits.
    """
    max_width = 0

    for char in digits:
        for line in digits[char]:
            value = len(line)
            if value > max_width:
                max_width = value

    return max_width


def standardize_width(digits, max_width):
    """Pad or truncate each line in each digit to `max_width` characters.

    This helps ensure columns align when composing multiple digits side-by-side.

    Args:
        digits (dict): Digit definitions mapping to 7-line lists.
        max_width (int): Desired line width for each digit line.

    Returns:
        dict: The adjusted digits dictionary.
    """
    for char in digits:
        corrected_lines = []

        for line in digits[char]:
            if len(line) < max_width:
                corrected_line = line + (' ' * (max_width - len(line)))
            elif len(line) > max_width:
                corrected_line = line[:max_width]
            else:
                corrected_line = line

            corrected_lines.append(corrected_line)

        digits[char] = corrected_lines

    return digits