import argparse

def parse(flags=None):
    parser = argparse.ArgumentParser(
        description='Query Pokemon API from the terminal',
        epilog='Gotta catch\'em all!!!'
    )

    parser.add_argument(
        'resource',
        choices=['card', 'set', 'types', 'subtypes', 'supertypes', 'rarities'], 
        help='the resource you are looking for'
    )

    parser.add_argument(
        '-i',
        '--id', 
        metavar='ID',
        help='the id or ids of cards you are looking for'
    )

    parser.add_argument(
        '-q',
        '--query', 
        metavar='Q',
        help='the query for cards you are looking for'
    )

    if flags:
        return vars(parser.parse_args(flags))
    else:
        return vars(parser.parse_args())

if __name__ == '__main__':
    print(parse())