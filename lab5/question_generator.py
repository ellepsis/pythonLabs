import random

import requests

import server

import re


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

    def set_complexity_range(self, complexity_range: int):
        if complexity_range < 2 or complexity_range > 100:
            raise Exception("Complexity range must be in range 2..100")
        self.complexity_range = complexity_range

    def generate_question(self, complexity_range: int):
        ids = set()
        while len(ids) <= self.variations:
            ids.add(random.randint(1, len(self.names)))
        names = [self.names[x] for x in ids]

        name_id = random.randint(0, len(names)-1)
        name = names[name_id]
        link = self.__google_request(name, complexity_range)

        question_id = self.last_question_id
        self.last_question_id += 1
        self.questions[question_id] = (name_id, name)
        return question_id, names, link

    def check_answer(self, question_id, answer):
        res = (self.questions[question_id][0] == answer)
        self.questions.pop(question_id)
        return res

    @staticmethod
    def __google_request(name: str, complexity_range: int):

        res = random.randint(1, int(complexity_range))
        entry = res%20
        page = int(res/20)
        headers = {
            'User-Agent': 'My User Agent 1.0',
            'From': 'vasya123@domain.com'  # This is another valid field
        }
        req = "https://www.google.ru/search?tbm=isch&q=" + name + "&start=" + str(page*20)
        r = requests.get(req, headers=headers)
        urls = re.findall(r'<img.*?src=\"(.*?)\">', r.text)
        return urls[entry]
        #TODO MUST SELECT image in range : 0 .. complexity_range
        #return "http://cs4.pikabu.ru/images/big_size_comm/2014-04_5/13983931397644.png"
