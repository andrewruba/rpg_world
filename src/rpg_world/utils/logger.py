import logging
import os

class Logger:
    """
    A simple logger class to handle logging across the RPG framework.
    """

    def __init__(self, name: str, log_file: str = "game_log.log", log_level=logging.INFO):
        """
        Initialize the logger.

        Args:
            name (str): The name of the logger.
            log_file (str): The file where logs will be saved.
            log_level (int): The logging level (e.g., logging.DEBUG, logging.INFO).
        """
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up the logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # File handler for writing logs to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Console handler for output to the terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Formatter to define the log format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Adding handlers to the logger
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)

    def info(self, message: str):
        """Log an info message."""
        self.logger.info(message)

    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message: str):
        """Log a critical message."""
        self.logger.critical(message)
