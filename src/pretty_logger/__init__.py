#  Author:      Davide Alejandro Castejon (aka Kayer)
#               devkayer@gmail.com

from time import time
from datetime import datetime
from sys import argv, __stdout__

from pretty_logger.constants import BColors
from pretty_logger.file_logger import FileLogger


def stringify_args(args: tuple[any, ...]) -> str:
    """
    Takes multiple arguments of any type and converts them into a single concatenated string

    :param args: list of arguments
    :return: Concatenated str
    """
    output: str = ''

    for var in args:
        if type(var) is str:
            output += var + ' '
        else:
            output += str(var) + ' '

    return output


class Logger:
    NAME: str
    """The name of the logger"""

    CMDS: str
    """The commands from the system arguments for the logger"""

    FILE_LOGGER: FileLogger | None = None
    """The file logger object for the logger. Can be None if no file logger is configured"""

    def __init__(self, name: str):
        """
        Logger object to be used in substitution to "normal" __stdout__.write statements in OOP style programming.
        It is built to almost simulates the behaviour of the logger found in nest.js

        :param name: Name for the logger. Usually will be the same as the object calling it
        """
        self.NAME = f'[{BColors.BOLD}{name.upper()}{BColors.END_C}]'
        self.CMDS = ''

        if len(argv) > 1:
            for cmd in argv[1:]:
                if cmd == '--pretty-debug':
                    self.CMDS += 'd'

                if cmd == '--pretty-error':
                    self.CMDS += 'e'

                if cmd == '--pretty-save':
                    self.FILE_LOGGER = FileLogger(name)

                if cmd == '--pretty-all':
                    self.CMDS = 'de'
                    break

                if cmd == '--pretty-none':
                    self.CMDS = 'n'
                    break

                if cmd == '--pretty-save-silent':
                    self.FILE_LOGGER = FileLogger(name)
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

    def internal_error(self, message: str, error: Exception) -> None:
        """
        Allows for logging of internal errors which may (but shouldn't happen) during the function execution.

        :param message: The original message to be outputted
        :param error: The error that the message caused
        """
        current = datetime.fromtimestamp(time())

        if self.FILE_LOGGER:
            self.FILE_LOGGER.save_internal_error(message, error, str(current))

        __stdout__.write(f'[INTERNAL {self.NAME} ERROR][{current}]\tFailed to output: "{message}" with error: "{error}"\n')

    def debug(self, *args: any) -> None:
        """
        Given the debug format, displays in the terminal the text received.
        Formats for "debug" warn logs

        :param args: list of arguments to display
        """
        text: str = stringify_args(args)

        if self.FILE_LOGGER:
            self.FILE_LOGGER.save_debug(text)

        if 'd' not in self.CMDS or 'n' in self.CMDS:
            return

        current = datetime.fromtimestamp(time())
        start = f'{self.NAME}{BColors.WARNING}[{current}][DEBUG]:\t'

        try:
            __stdout__.write(f'{start}{str(text)}{BColors.END_C}\n')
        except TypeError as e:
            self.internal_error(text, e)

    def error(self, *args: any) -> None:
        """
        Given the error format, displays in the terminal the text received.
        Formats for "error" logs.

        :param args: list of arguments to display
        """
        text: str = stringify_args(args)

        if self.FILE_LOGGER:
            self.FILE_LOGGER.save_error(text)

        if 'n' in self.CMDS or 'e' not in self.CMDS:
            return

        current = datetime.fromtimestamp(time())
        start = f'{self.NAME}{BColors.FAIL}[{current}][ERROR]:\t'

        try:
            __stdout__.write(f'{start}{str(text)}{BColors.END_C}\n')
        except TypeError as e:
            self.internal_error(text, e)

    def log(self, *args: any) -> None:
        """
        Given the log format, displays in the terminal the text received.
        Formats for "normal" logs.

        :param args: list of arguments to display
        """
        text: str = stringify_args(args)

        if self.FILE_LOGGER:
            self.FILE_LOGGER.save_log(text)

        if 'n' in self.CMDS:
            return

        current = datetime.fromtimestamp(time())
        start = f'{self.NAME}{BColors.OK_GREEN}[{current}][LOG]:\t'

        try:
            __stdout__.write(f'{start}{str(text)}{BColors.END_C}\n')
        except TypeError as e:
            self.internal_error(text, e)
