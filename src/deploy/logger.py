import os
from loguru import logger

# Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Define log file path
LOG_FILE = os.path.join(LOG_DIR, "deploy.log")

# Get log level from environment variables (default: INFO)
LOG_LEVEL = os.getenv("DEPLOY_LOG_LEVEL", "INFO").upper()

# Remove any existing log handlers before adding new ones
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
    rotation="10 MB",  # Rotate logs every 10MB
    compression="zip",  # Compress old logs
    retention="30 days"  # Keep logs for 30 days
)

def get_logger():
    """Returns the global logger instance."""
    return logger
