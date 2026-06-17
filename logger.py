import logging
import os
from datetime import datetime

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Get current working directory (STRING, not bytes)
curr_dir = os.getcwd()

# Create logs directory path
logs_dir = os.path.join(curr_dir, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s %(levelname)s %(name)s [line:%(lineno)d] %(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")