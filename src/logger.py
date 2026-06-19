import logging
import os
from datetime import datetime

# Log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Stable base directory
curr_dir = os.path.dirname(os.path.abspath(__file__))

# Logs directory
logs_dir = os.path.join(curr_dir, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s | %(levelname)s | %(name)s | line:%(lineno)d | %(message)s",
    level=logging.INFO,
    force=True
)