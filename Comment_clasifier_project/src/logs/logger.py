import logging
import os

# Define the log file path
LOG_FILE = r'src\logs\data_append.log'

# Ensure the logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format='%(asctime)s — %(levelname)s — %(message)s'
)

# Create a logger instance
logger = logging.getLogger(__name__)
logger.info("Logger initialized and ready to capture logs.")

"""
Logger module.

This module configures and initializes a logger instance
for consistent logging across the project.

Attributes
----------
logger : logging.Logger
    Configured logger instance that writes logs to 'src/logs/data_append.log'.
"""
