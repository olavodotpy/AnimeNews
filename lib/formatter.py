from feedsrss import Posts


rss = Posts() # test

class Form:
    
    def __init__(self):
        self.initial_content = ""
        self.iddle_content = ""
        self.final_content = ""
        self.log_content = []
        self.log_log_content = [] # fix the log log
        self.filters = {

            "initial": {
                "f1": "RELACIONADO:",
                "f2": "RELACIONADO :",
                "f3": "RELACIONADO",
            },
            # "iddle": {
            #     "f1": "Fonte:",
            #     "f2": "Fonte" ,
            #     "f3": "Fontes:",
            #     "f4": "Fontes",
            # },
            "iddle": {
                "f1": "produção",
            },
        }


    def filter_initial(self, b_content: str):
        word_group = b_content.split()
        f = self.filters['initial']['f1']
        # test each filter one by one

        if f in word_group:
            i = word_group.index(f)

            while i < len(word_group):
                self.log_content.append(word_group[i])
                word_group.pop(i)
            
        self.initial_content = " ".join(word_group)
        return self.initial_content


    def filter_iddle(self):
        # self.log_content = self.log_content[:]
        f = self.filters['iddle']['f1']

        if f in self.log_content:
            i = self.log_content.index(f)

            while i < len(self.log_content):
                self.log_log_content.append(self.log_content[i])
                self.log_content.pop(i)
            
        self.iddle_content = " ".join(self.log_content)
        print(self.log_log_content)
        return self.iddle_content
    

    def filter_final(self):
        pass


if __name__ == "__main__":

    # test

    test = Form()

    posts = rss.get_posts()
    textS = ""

    for post in posts:
        textS = post['content']
        break


    result = test.filter_initial(textS)
    result2 = test.filter_iddle()
    print(result)
    print(result2)
