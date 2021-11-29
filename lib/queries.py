

def build_query(args):
    if args['id']:
        return args['id']
    else:
        return args['query']

