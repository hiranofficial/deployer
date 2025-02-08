import os
from loguru import logger
from deploy.config import Config

# Load configuration
config = Config()
LOG_LEVEL = config.get("logging", "log_level", "INFO").upper()
LOG_FILE = config.get("logging", "log_file", "logs/deploy.log")

# Ensure the logs directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Remove any existing log handlers
logger.remove()

# Add console logging
logger.add(
    sink=lambda msg: print(msg, end=""),  # Console output
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>",
    level=LOG_LEVEL,
    colorize=True
)

# Add file logging
logger.add(
    LOG_FILE,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level=LOG_LEVEL,
    rotation="10 MB",
    compression="zip",
    retention="30 days"
)

def get_logger():
    """Returns the global logger instance."""
    return logger
