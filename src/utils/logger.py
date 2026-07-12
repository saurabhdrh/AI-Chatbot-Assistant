"""Application logging setup.

Importing this module configures the root logger to write to
``logs/chatbot.log`` and exposes a ready-to-use ``logger`` instance.
"""

import logging
from pathlib import Path

# Create the logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/chatbot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)