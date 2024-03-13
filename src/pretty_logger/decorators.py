import builtins
from pretty_logger import Logger


def pretty_log(func):
    """
    Decorator to change all the print statements inside the function to the pretty_logger.log function.
    """
    logger: Logger = Logger(func.__name__.upper())
    original_print = builtins.print
    builtins.print = logger.log

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper


def pretty_debug(func):
    """
    Decorator to change all the print statements inside the function to the pretty_logger.debug function.
    """
    logger: Logger = Logger(func.__name__.upper())
    original_print = builtins.print
    builtins.print = logger.debug

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper


def pretty_error(func):
    """
    Decorator to change all the print statements inside the function to the pretty_logger.error function.
    """
    logger: Logger = Logger(func.__name__.upper())
    original_print = builtins.print
    builtins.print = logger.error

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print

    return wrapper
