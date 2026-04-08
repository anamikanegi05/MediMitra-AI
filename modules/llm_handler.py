class LLMHandler:
    def __init__(self):
        self.data_store = []

    def store_input(self, text):
        self.data_store.append(text)
