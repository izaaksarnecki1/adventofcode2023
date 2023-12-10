import os
class GetContent:
    def __init__(self, nr):
        self.nr = nr
    
    def get_content(self):
        with open(f'{self.nr}', 'r') as f:
            content = f.read()
        return content
