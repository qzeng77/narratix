import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from src.config.settings import BASE_DIR

def setup_logger(name: str = 'ai_rpg'):
    """Configure and return a logger instance"""
    # Create logs directory if it doesn't exist
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    
    # Create logger instance
    logger = logging.getLogger(name)
    logger.setLevel(logging.WARNING)  

    # Configure formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)  
    console_handler.setFormatter(formatter)
    
    # File handler
    file_handler = logging.FileHandler(f'{BASE_DIR}/logs/ai_rpg.log')
    file_handler.setLevel(logging.WARNING)  
    file_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# Create default logger instance
logger = setup_logger()