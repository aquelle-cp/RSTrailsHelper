from clue import AnagramClue
from clue import CoordClue
from clue import CrypticClue
import sys

# Main
def main():
    anagrams = fill_anagram()
    coordinates = fill_coord()
    cryptics = fill_cryptic()
    usage = '''usage: [clue || usage || q]
        q - quit
        usage - print usage message\n'''

    # Goal: print out all matching results in format
    # clue text | solution | location

    # Get input until message to exit
    print(usage)
    while(True):
        find = input('clue: ')

        # Check for exit before searching
        if find == 'q':
            sys.exit()
        elif find == 'usage':
            print(usage)
        else:
            find = find.lower()
            match_anagrams = [a for a in anagrams if find in a.clue_text]
            match_coordinates = [c for c in coordinates if find in c.clue_text]
            match_cryptics = [y for y in cryptics if find in y.clue_text]

            print('')

            # Print matching anagrams
            if match_anagrams:
                print('Anagrams:')

                for a in match_anagrams:
                    print(f'| {a.clue_text:32} | {a.solution:32} | {a.challenge:2} | \n| {a.location}')

                print('')

            # Print matching coordinates
            if match_coordinates:
                print('Coordinates:')

                for c in match_coordinates:
                    print(f'| {c.clue_text:11} | {c.location}')

                print('')

            # Print matching cryptics
            if match_cryptics:
                print('Cryptics:')

                for y in match_cryptics:
                    if y.key == '-':
                        print(f'| {y.short_ver:32} | {y.location}')
                    else:
                        print(f'| {y.short_ver:32} | {y.location:32} | {y.key}')

                print('')

            # If there aren't any matches, notify user
            if not match_anagrams and not match_coordinates and not match_cryptics:
                print('No matching clues')

        print('')


# Create a list of AnagramClue objects and fill from file
def fill_anagram():
    file = open('anagrams.txt', 'r')
    anagrams = []

    count = 0
    for line in file:
        if count % 5 == 0:
            text = line.rstrip('\n').lower()
        elif count % 5 == 1:
            sol = line.rstrip('\n')
        elif count % 5 == 2:
            ch = line.rstrip('\n')
        elif count % 5 == 3:
            loc = line.rstrip('\n')
            anagrams.append(AnagramClue(text, sol, ch, loc))

        count += 1

    file.close()

    return anagrams

# Create a list of CoordClue objects and fill from file
def fill_coord():
    file = open('coordinates.txt', 'r')
    coordinates = []

    count = 0
    for line in file:
        if count % 4 == 0:
            num = line.rstrip('\n')
        elif count % 4 == 1:
            text = line.rstrip('\n')
        elif count % 4 == 2:
            loc = line.rstrip('\n')
            coordinates.append(CoordClue(num, text, loc))

        count += 1

    file.close()

    return coordinates

# Create a list of CrypticClue objects and fill from file
def fill_cryptic():
    file = open('cryptic.txt', 'r')
    cryptics = []

    count = 0
    for line in file:
        if count % 5 == 0:
            text = line.rstrip('\n').lower()
        elif count % 5 == 1:
            short = line.rstrip('\n')
        elif count % 5 == 2:
            loc = line.rstrip('\n')
        elif count % 5 == 3:
            key = line.rstrip('\n')
            cryptics.append(CrypticClue(text, short, loc, key))

        count += 1

    file.close()

    return cryptics

if __name__ == '__main__':
    main()
