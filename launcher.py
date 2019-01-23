import sys
import string
import argparse
from dict_generator import Generator
from format_generator import FormatGenerator
from fullname_parsing import Parser
from utils import get_file_contents


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


        p = Parser(args.fullname_file, args.fullname_format).parse_fullname_file()

        names = p.get('name', None)
        surnames = p.get('surname', None)
        patronymics = p.get('patronymic', None)

    else:
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
