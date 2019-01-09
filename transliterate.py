import re
import json


class Transliterator:
    def __init__(self, config):
        self.config = config

    def convert(self, string):
        with open(self.config) as w:
            lower_case_letters = json.loads(w.read())

        constructed = [""]
        
        for letter in string:
            tmp_result = []

            for substitute_letter in lower_case_letters.get(letter, (letter,)):
                current_result = list(
                    list(map(
                        lambda word: word + substitute_letter,
                        constructed
                    )),
                )
                tmp_result += current_result

            constructed = tmp_result

        return constructed
