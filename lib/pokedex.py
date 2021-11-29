import commandline
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from queries import build_query




def main():
    args = commandline.parse()

    if args['id']:
        card = Card.find(args['id'])
        print(card.name)
    else:
        cards = Card.where(q=args['query'])

        for card in cards:
            print(card.name)

    print(args)
    
    
if __name__ == '__main__':
    main()