class Formatter:
    
    def __init__(self, word_group: str):
        self.word_group = word_group.split()
        self.cache = []
        self.result = ""


    def content_filters(self, grille: str):
        if grille in self.word_group:
            
            self.cache.clear()
            
            while self.word_group[0] != grille:
                removed_item = self.word_group.pop(0)
                self.cache.append(removed_item)
            
            self.result = " ".join(self.cache)
            return self.result
        
        return self.result
