import logging

def setup_logger():
    try:
        # Create a logger
        logger = logging.getLogger("Cfprac2")
        
        # Set logging level to ALL (which is DEBUG in Python, as it captures all levels)
        logger.setLevel(logging.DEBUG)
        
        # Create a file handler to log messages to a file
        file_handler = logging.FileHandler("./mylogfile.log", mode='a')  # 'a' means append mode
        
        # Create a simple formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Apply the formatter to the handler
        file_handler.setFormatter(formatter)
        
        # Add the handler to the logger
        logger.addHandler(file_handler)
        
        return logger
    except Exception as e:
        print(f"Error setting up logger: {e}")
        return None

def main():
    logger = setup_logger()
    
    if logger is not None:
        # Log some messages
        logger.info("My first log")
        logger.info("This is CFL Prac 2")
    else:
        print("Logger could not be initialized")

if __name__ == "__main__":
    main()
