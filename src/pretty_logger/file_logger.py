#  Author:      Davide Alejandro Castejon (aka Kayer)
#               devkayer@gmail.com

from datetime import datetime
from time import time
from os import path, makedirs, listdir
from shutil import rmtree
from sys import argv

from pretty_logger.constants import PREFIX


def save_to_file(file_path: str, message: str) -> None:
    """
    Append the message to the specified file.

    :param file_path: Path to the file to write in
    :param message: The message to append to the file
    """
    with open(file_path, "w") as log_file:
        log_file.write(f'{message}\n')
        log_file.close()


class FileLogger:
    folder_path: str
    """Folder path to where the log files will be stored"""

    name: str
    """Name of the class running this file logger"""

    def __init__(self, name: str):
        """
        Log system which saves the logs into specific text files.

        :param name: Name of the class that invoked the Logger.
        """
        self.name = name

        if len(argv) > 1:
            for i, arg in enumerate(argv):
                if arg == "--logger-folder-path":
                    self.folder_path = path.join(argv[i + 1])
                    break
                else:
                    self.folder_path = path.join('./logs/')
        else:
            self.folder_path = path.join('./logs/')

        if not path.exists(self.folder_path):
            makedirs(self.folder_path)

        if not path.isdir(self.folder_path):
            rmtree(self.folder_path)
            makedirs(self.folder_path)

        if PREFIX[0] == -1:
            max_prefix: int = -1
            for name in listdir(self.folder_path):
                entity = path.join(self.folder_path, name)
                if path.isdir(entity):
                    prefix: str = name
                    max_prefix = int(prefix) if int(prefix) > max_prefix else max_prefix

            self.prefix = max_prefix + 1
            PREFIX[0] = max_prefix

            self.folder_path = path.join(self.folder_path, "{:03}".format(self.prefix))
            makedirs(self.folder_path)
            makedirs(path.join(self.folder_path + "/log/"))
            makedirs(path.join(self.folder_path + "/debug/"))
            makedirs(path.join(self.folder_path + "/error/"))
        else:
            self.prefix = PREFIX[0]
            self.folder_path = path.join(self.folder_path, "{:03}".format(self.prefix))

    def save_internal_error(self, message: str, error: Exception, timestamp: str) -> None:
        """
        Saves internal error messages from the Logger class.

        :param message: The message that was attempted to be logged
        :param error: The error that was caused by the attempted message
        :param timestamp: The timestamp when the error happened
        """
        file_path = path.join(self.folder_path, 'internal_errors.txt')
        log: str = f'[INTERNAL {self.name} ERROR][{timestamp}]\tFailed to output: "{message}" with error: "{error}"'

        save_to_file(file_path, log)

    def save_log(self, log: str) -> None:
        """
        Saves the log message from the Logger class into the logs text file.

        :param log: Message to be formatted and saved
        """
        file_path = f'{self.folder_path}/log/{self.name}_class_logs.txt'

        current = datetime.fromtimestamp(time())
        save_to_file(file_path, f'[{current}]: {log}')

    def save_debug(self, log: str) -> None:
        """
        Saves the log message from the Logger class into the debug text file.

        :param log: Message to be formatted and saved
        """
        file_path = f'{self.folder_path}/debug/{self.name}_class_logs.txt'

        current = datetime.fromtimestamp(time())
        save_to_file(file_path, f'[{current}]: {log}')

    def save_error(self, log: str) -> None:
        """
        Saves the log message from the Logger class into the errors text file.

        :param log: Message to be formatted and saved
        """
        file_path = f'{self.folder_path}/error/{self.name}_class_logs.txt'

        current = datetime.fromtimestamp(time())
        save_to_file(file_path, f'[{current}]: {log}')

