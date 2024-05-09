#  Author:      Davide Alejandro Castejon (aka Kayer)
#               devkayer@gmail.com

import builtins
from pretty_logger import Logger


def pretty_log(func):
    """
    Decorator to change all the print statements inside the function to the pretty_logger.log function.
    """

    def wrapper(*args, **kwargs):
        logger: Logger = Logger(func.__name__.upper())
        original_print = builtins.print
        builtins.print = logger.log

        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper


def pretty_debug(func):
    """
    Decorator to change all the print statements inside the function to the pretty_logger.debug function.
    """

    def wrapper(*args, **kwargs):
        logger: Logger = Logger(func.__name__.upper())
        original_print = builtins.print
        builtins.print = logger.debug

        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper


def pretty_error(func):
    """
    Decorator to change all the print statements inside the function to the pretty_logger.error function.
    """

    def wrapper(*args, **kwargs):
        logger: Logger = Logger(func.__name__.upper())
        original_print = builtins.print
        builtins.print = logger.error

        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper
