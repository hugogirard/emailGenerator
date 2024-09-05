

class OpenAI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAI, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
          pass