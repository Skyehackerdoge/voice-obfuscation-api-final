import logging

def configure_logging():
    # Keep logging readable and simple for production debugging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
