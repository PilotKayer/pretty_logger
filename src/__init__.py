from time import time
from datetime import datetime
from sys import argv

from src.colors import BColors


class Logger:
    NAME: str
    """The name of the logger"""

    CMDS: str
    """The commands from the system arguments for the logger"""

    def __init__(self, name: str):
        """
        Logger object to be used in substitution to "normal" print statements in OOP style programming.
        It is built to almost simulates the behaviour of the logger found in nest.js

        :param name: Name for the logger. Usually will be the same as the object calling it
        """
        self.NAME = f'[{BColors.BOLD}{name}{BColors.END_C}]'

        if len(argv) > 1:
            for cmd in argv[1:]:
                if cmd == '--pretty-debug':
                    self.CMDS += 'd'

                if cmd == '--pretty-error':
                    self.CMDS += 'e'

                if cmd == '--pretty-none':
                    self.CMDS += 'n'
                    break
        else:
            self.CMDS = 'e'

    def get_name(self) -> str:
        """
        Returns the name associated to the logger

        :return: The NAME of the logger
        """
        return self.NAME

    def get_commands(self) -> str:
        """
        Returns the commands associated to the logger

        :return: The CMDS of the logger
        """
        return self.CMDS

    def debug(self, text: str) -> None:
        """
        Given the debug format, displays in the terminal the text received.
        Formats for "debug" warn logs

        :param text: The text to display
        """
        if 'd' not in self.CMDS or 'n' in self.CMDS:
            return

        current = datetime.fromtimestamp(time())
        start = f'{self.NAME}{BColors.WARNING}[{current}][DEBUG]:\t'

        try:
            print(f'{start}{str(text)}{BColors.END_C}')
        except TypeError:
            return

    def error(self, text: str) -> None:
        """
        Given the error format, displays in the terminal the text received.
        Formats for "error" logs.

        :param text: The text to display
        """
        if 'n' in self.CMDS or 'e' not in self.CMDS:
            return

        current = datetime.fromtimestamp(time())
        start = f'{self.NAME}{BColors.FAIL}[{current}][ERROR]:\t'

        try:
            print(f'{start}{str(text)}{BColors.END_C}')
        except TypeError:
            return

    def log(self, text: str) -> None:
        """
        Given the log format, displays in the terminal the text received.
        Formats for "normal" logs.

        :param text: The text to display
        """
        if 'n' in self.CMDS:
            return

        current = datetime.fromtimestamp(time())
        start = f'{self.NAME}{BColors.OK_GREEN}[{current}][LOG]:\t'

        try:
            print(f'{start}{str(text)}{BColors.END_C}')
        except TypeError:
            return
