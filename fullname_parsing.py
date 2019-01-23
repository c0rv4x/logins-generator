import string
from utils import get_file_contents


class Parser:
    def __init__(self, fullname_file, fullname_format):
        self.fullname_file = fullname_file
        self.fullname_format = fullname_format

        self.delimiters = None


    def parse_fullname_file(self):
        self.extract_delimiters()
        self.extract_parameters_name()
        self.extract_data_by_delimiters()

        return self.build_dictionary()


    def extract_delimiters(self):
        self.delimiters = []
        delimiter_already = False

        for i, letter in enumerate(self.fullname_format):
            if letter not in string.ascii_lowercase:
                if delimiter_already:
                    self.delimiters[-1] = (self.delimiters[-1][0], self.delimiters[-1][1] + letter)
                else:
                    delimiter_already = True
                    self.delimiters.append((i, letter))
            else:
                delimiter_already = False


    def extract_parameters_name(self):
        start = 0
        self.parameters_names = []

        for delimiter_index, delimiter in self.delimiters:
            self.parameters_names.append(self.fullname_format[start:delimiter_index])
            start = delimiter_index + len(delimiter)

        self.parameters_names.append(self.fullname_format[start:])


    def extract_data_by_delimiters(self):
        data = get_file_contents(self.fullname_file)

        self.result = []
        for i in range(0, len(self.delimiters) + 1):
            self.result.append([])

        for line in data:
            cut_line = line

            for i, x in enumerate(self.delimiters):
                _, delimiter = x
                part_end_index = cut_line.index(delimiter)
                self.result[i].append(cut_line[0 : part_end_index])
                cut_line = cut_line[part_end_index + len(delimiter) : ]
            self.result[i + 1].append(cut_line)

    def build_dictionary(self):
        formed_dict = {}

        for i in range(0, len(self.parameters_names)):
            key = self.parameters_names[i]
            value = self.result[i]
            formed_dict[key] = value

        return formed_dict
