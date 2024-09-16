import logging
import pytest
from rpg_world import Logger

@pytest.fixture
def setup_logger():
    """Fixture to set up a logger."""
    logger_name = "test_logger"
    logger = Logger(name=logger_name, log_level=logging.DEBUG)
    return logger

def test_logger_debug_message(setup_logger, caplog):
    """Test logging a debug message."""
    logger = setup_logger
    
    with caplog.at_level(logging.DEBUG):
        logger.debug("Debug message for testing.")

    # Check that the message was logged
    assert "Debug message for testing." in caplog.text
    assert "DEBUG" in caplog.text

def test_logger_info_message(setup_logger, caplog):
    """Test logging an info message."""
    logger = setup_logger
    
    with caplog.at_level(logging.INFO):
        logger.info("Info message for testing.")

    # Check that the message was logged
    assert "Info message for testing." in caplog.text
    assert "INFO" in caplog.text

def test_logger_warning_message(setup_logger, caplog):
    """Test logging a warning message."""
    logger = setup_logger
    
    with caplog.at_level(logging.WARNING):
        logger.warning("Warning message for testing.")

    # Check that the message was logged
    assert "Warning message for testing." in caplog.text
    assert "WARNING" in caplog.text

def test_logger_error_message(setup_logger, caplog):
    """Test logging an error message."""
    logger = setup_logger
    
    with caplog.at_level(logging.ERROR):
        logger.error("Error message for testing.")

    # Check that the message was logged
    assert "Error message for testing." in caplog.text
    assert "ERROR" in caplog.text

def test_logger_critical_message(setup_logger, caplog):
    """Test logging a critical message."""
    logger = setup_logger
    
    with caplog.at_level(logging.CRITICAL):
        logger.critical("Critical message for testing.")

    # Check that the message was logged
    assert "Critical message for testing." in caplog.text
    assert "CRITICAL" in caplog.text
