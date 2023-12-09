import os
class GetContent:
    def __init__(self):
        self.file = 'input.txt'
        self.filename = os.path.join(os.path.dirname(__file__), self.file)
    
    def get_content(self):
        with open(self.filename, 'r') as f:
            content = f.read()
        return content
