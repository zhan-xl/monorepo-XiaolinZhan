class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print('Logger created exactly once')
            cls.instance = super(Logger, cls).__new__(cls)
        else:
            print('Logger already created')
        return cls.instance
    
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
