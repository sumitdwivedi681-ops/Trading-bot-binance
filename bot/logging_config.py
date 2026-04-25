import logging
import os

def setup_logging():
    logging.basicConfig(
        filename="logs/trading.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
