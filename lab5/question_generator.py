import random

import server


class QuestionGenerator:
    names = []
    questions = {}
    last_question_id = 0
    variations = 5

    def __init__(self, names_filename: str, variations):
        self.__read_names_file(names_filename)
        self.variations = variations

    def __read_names_file(self, file: str):
        content = server.read_file(file)
        self.names = content.split("\n")

    def generate_question(self):
        ids = set()
        while len(ids) <= self.variations:
            ids.add(random.randint(1, len(self.names)))
        names = [self.names[x] for x in ids]

        name_id = random.randint(0, len(names)-1)
        name = names[name_id]
        link = self.__google_request(name)

        question_id = self.last_question_id
        self.last_question_id += 1
        self.questions[question_id] = (name_id, name)
        return question_id, names, link

    def check_answer(self, question_id, answer):
        res = (self.questions[question_id][0] == answer)
        self.questions.pop(question_id)
        return res

    @staticmethod
    def __google_request(name: str):
        #req = "https://www.google.ru/search?tbm=isch&q=" + name
        #r = requests.get(req)
        #return r
        return "http://cs4.pikabu.ru/images/big_size_comm/2014-04_5/13983931397644.png"
