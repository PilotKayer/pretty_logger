#  Author:      Davide Alejandro Castejon (aka Kayer)
#               devkayer@gmail.com

class BColors:
    """
    Stores the constants with the codes to change the colors of text in the terminal
    """
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


PREFIX: list[int] = [-1]
"""Job prefix to save the logger to. Using a list as lists are mutable variables in python."""

