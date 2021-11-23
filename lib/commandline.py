import argparse

def parse(flags=None):
    parser = argparse.ArgumentParser(description='Process pokemon card details')

    parser.add_argument(
        '--id', 
        metavar='id',
        type=str,
        nargs='+',
        help='the id or ids of cards you are looking for'
    )

    if flags:
        return vars(parser.parse_args(flags))
    else:
        return vars(parser.parse_args())

if __name__ == '__main__':
    print(parse())