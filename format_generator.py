import re


# class FormatGenerator:
#     def __init__(self, formating):
#         self.formating = None
#         self.argument_functions = []
#         self.parse_format(formating)

#     def parse_format(self, formating):
#         self.formating = formating
#         extracted_formats = re.findall(r'(\{([a-z]+)(\[[0-9]+\]){0,1}\})', formating)

#         for raw_format, param_name, raw_index in extracted_formats:
#             self.formating = self.formating.replace(raw_format, '{}')

#             if raw_index:
#                 index = int(raw_index[1:-1])
#                 self.argument_functions.append(lambda input_dict: input_dict[param_name][index])
#             else:
#                 self.argument_functions.append(lambda input_dict: input_dict[param_name])


class FormatGenerator:
    def __init__(self, formating):
        self.formating = formating

    def format_string(self, **kwargs):
        return self.formating.format(**kwargs)