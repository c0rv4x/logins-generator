import sys
import string
import argparse
from dict_generator import Generator
from format_generator import FormatGenerator


def get_file_contents(filename):
    with open(filename) as w:
        return w.read().strip().split()


def extract_delimiters(fullname_format):
    delimiters = []
    delimiter_already = False

    for i, letter in enumerate(fullname_format):
        if letter not in string.ascii_lowercase:
            if delimiter_already:
                delimiters[-1] = (delimiters[-1][0], delimiters[-1][1] + letter)
            else:
                delimiter_already = True
                delimiters.append((i, letter))
        else:
            delimiter_already = False

    return delimiters

def extract_parameters_name(delimiters, fullname_format):
    start = 0
    end_parameters = []

    for delimiter_index, delimiter in delimiters:
        end_parameters.append(fullname_format[start:delimiter_index])
        start = delimiter_index + len(delimiter)

    end_parameters.append(fullname_format[start:])

    return end_parameters

def parse_fullname_file(fullname_file, fullname_format):
    delimiters = extract_delimiters(fullname_format)
    end_parameters = extract_parameters_name(delimiters, fullname_format)

    # Parsing full input file
    data = get_file_contents(fullname_file)

    result = []
    for i in range(0, len(end_parameters) + 1):
        result.append([])

    for line in data:
        cut_line = line

        for i, x in enumerate(delimiters):
            _, delimiter = x
            part_end_index = cut_line.index(delimiter)
            result[i].append(cut_line[0 : part_end_index])
            cut_line = cut_line[part_end_index + len(delimiter) : ]
        result[i + 1].append(cut_line)

    formed_dict = {}
    for i in range(0, len(end_parameters)):
        key = end_parameters[i]
        value = result[i]
        formed_dict[key] = value

    print(formed_dict)




if __name__== "__main__":
    parser = argparse.ArgumentParser(description='Generate list of nicknames by certain format')
    parser.add_argument('formating', type=str, nargs=1,
                        help='format string (use {name}, {surname[2]}, {patronymic[5]} and constant strings)')
    parser.add_argument('--name', type=str, nargs='+',
                        help='first name (multiple, space-delimited)')
    parser.add_argument('--name-file', type=str, dest='name_file',
                        help='first names file')

    parser.add_argument('--surname', type=str, nargs='+',
                        help='surname (multiple, space-delimited)')
    parser.add_argument('--surname-file', type=str, dest="surname_file",
                        help='surnames file')

    parser.add_argument('--patronymic', type=str, nargs='+',
                        help='patronymic (multiple, space-delimited)')
    parser.add_argument('--patronymic-file', type=str, dest="patronymic_file",
                        help='patronymics file')

    parser.add_argument('--fullname-file', type=str, dest="fullname_file",
                        help='fullname file (\n delimited entries)')
    parser.add_argument('--fullname-format', type=str, dest="fullname_format",
                        help='fullname file format, will be parsed into list of primitive parameters, e.x. name:surname:patronymic')

    parser.add_argument('--config', type=str, default="transliteration.json", dest="transliteration_config",
                    help='transliteration config file')


    args = parser.parse_args()
    formating = args.formating[0]
    config = args.transliteration_config
    
    if args.name and args.name_file:
        print("You should specify either --name of --name-file, not both")
        sys.exit(1)

    if args.surname and args.surname_file:
        print("You should specify either --surname of --surname-file, not both")
        sys.exit(1)

    if args.patronymic and args.patronymic_file:
        print("You should specify either --patronymic of --patronymic-file, not both")
        sys.exit(1)

    if args.fullname_file and (
        args.name or args.name_file or
        args.surname and args.surname_file or
        args.patronymic and args.patronymic_file
    ):
        print("You can specify either --fullname-file or {--name, --surname, --patronymic}")
        sys.exit(1)

    if args.fullname_file:
        if not args.fullname_format:
            print("Specify a format using --fullname-format 'name:surname:patronymic' for example")
            sys.exit(1)

        parse_fullname_file(args.fullname_file, args.fullname_format)

    if args.name_file:
        names = get_file_contents(args.name_file)
    else:
        names = args.name

    if args.surname_file:
        surnames = get_file_contents(args.surname_file)
    else:
        surnames = args.surname

    if args.patronymic_file:
        patronymics = get_file_contents(args.patronymic_file)
    else:
        patronymics = args.patronymic

    print('\n'.join(Generator(formating, config, names, surnames, patronymics).build_formatted()))
