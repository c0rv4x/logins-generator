import re
import json


def transliterate(string, config_file):
    with open(config_file) as w:
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
