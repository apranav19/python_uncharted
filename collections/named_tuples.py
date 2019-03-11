'''
    Named Tuples are immutable.
    Each data item stored in a named tuple can be accessed through a unique id.
'''
from collections import namedtuple

def main():
    # First define a named tuple
    Club = namedtuple('Club', ['name', 'city', 'country'])

    arsenal = Club('Arsenal', 'London', 'UK')
    real_madrid = Club('Real Madrid', 'Madrid', 'Spain')
    borussia_dortmund = Club('Borussia Dortmund', 'Dortmund', 'Germany')

    clubs = [arsenal, real_madrid, borussia_dortmund]

    for club in clubs:
        print('Name: {0}\tCity: {1}\tCountry: {2}\n'.format(club.name, club.city, club.country))

if __name__ == '__main__':
    main()
    '''
        Expected output:
            Name: Arsenal	City: London	Country: UK

            Name: Real Madrid	City: Madrid	Country: Spain

            Name: Borussia Dortmund	City: Dortmund	Country: Germany
    '''
