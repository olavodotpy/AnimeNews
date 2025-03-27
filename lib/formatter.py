class Formatter:
    
    def __init__(self, word_group: str):
        self.word_group = word_group.split()
        self.cache = []
        self.response_content = ""


    def _filter(self, grille: str):
        if grille not in self.word_group:
            return False

        self.cache.clear()
        
        while self.word_group[0] != grille:
            removed_item = self.word_group.pop(0)
            self.cache.append(removed_item)
        
        self.response_content = " ".join(self.cache)
        return self.response_content
