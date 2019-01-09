import copy
from format_generator import FormatGenerator


class Combinations:
    def __init__(self):
        self.storage = []

    def populate_with_names(self, names):
        name_results = []
        for name in names:
            if self.storage:
                for params in self.storage:
                    new_params = copy.copy(params)
                    new_params['name'] = name
                    name_results.append(new_params)
            else:
                name_results.append({
                    "name": name,
                    "surname": None,
                    "patronymic": None
                })
        if names:
            self.storage = name_results

    def populate_with_surnames(self, surnames):
        surname_results = []
        for surname in surnames:
            if self.storage:
                for params in self.storage:
                    new_params = copy.copy(params)
                    new_params['surname'] = surname
                    surname_results.append(new_params)
            else:
                surname_results.append({
                    "name": None,
                    "surname": surname,
                    "patronymic": None
                })

        if surnames:
            self.storage = surname_results

    def populate_with_patronymics(self, patronymics):
        patronymic_results = []
        for patronymic in patronymics:
            if self.storage:
                for params in self.storage:
                    new_params = copy.copy(params)
                    new_params['patronymic'] = patronymic
                    patronymic_results.append(new_params)
            else:
                patronymic_results.append({
                    "name": None,
                    "surname": None,
                    "patronymic": patronymic
                })
        if patronymics:
            self.storage = patronymic_results

    def get_data(self):
        return self.storage

class Generator:
    def __init__(self, formating, names=None, surnames=None, patronymics=None):
        self.formating = formating
        self.names = names or []
        self.surnames = surnames or []
        self.patronymics = patronymics or []

        self.combinations = None
        self.build_combinations()

    def build_combinations(self):
        self.combinations = Combinations()
        self.combinations.populate_with_names(self.names)
        self.combinations.populate_with_surnames(self.surnames)
        self.combinations.populate_with_patronymics(self.patronymics)

    def build_formatted(self):
        formatter = FormatGenerator(self.formating)
        results = set()

        for combination in self.combinations.get_data():
            results.add(formatter.format_string(**combination))

        return list(results)
