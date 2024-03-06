import logging
import os
from datetime import datetime

# Define the log file name using the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path of the log folder
log_dir = r'D:\US-VISA-APPROVAL-PREDICTION\logs'

# Concatenate the log file path
logs_path = os.path.join(log_dir, LOG_FILE)

# Ensure that the log directory exists; create it if it doesn't
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
