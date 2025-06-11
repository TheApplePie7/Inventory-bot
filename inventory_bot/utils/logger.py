import logging

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,  # ✅ this must be DEBUG (not INFO)
        format='[%(asctime)s] [%(levelname)7s] %(name)s: %(message)s',
        handlers=[logging.StreamHandler()]
    )
    return logging.getLogger(__name__)
