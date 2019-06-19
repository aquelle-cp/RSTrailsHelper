from clue import AnagramClue
from clue import CoordClue
from clue import CrypticClue
from tkinter import *
from tkinter import ttk
import sys

# Main
def main():
    anagrams = fill_anagram()
    coordinates = fill_coord()
    cryptics = fill_cryptic()
    usage = '''usage: [type;clue]
    type options
        an - anagrams
        co - coordinates
        cr - cryptics

        qs - quit
        usage - print usage message\n'''

    # Goal: print out all matching results in format
    # clue text | solution | location

    # Get input until message to exit
    print(usage)
    while(True):
        find = input('clue: ')

        # Check for exit before searching
        if find == 'qs':
            sys.exit()
        elif find == 'usage' or len(find) < 4:
            print(usage)
        else:
            check = find[3:]
            match_anagrams = [a for a in anagrams if check in a.clue_text]
            match_coordinates = [c for c in coordinates if check in c.clue_text]
            match_cryptics = [y for y in cryptics if check in y.clue_text]

            for a in match_anagrams:
               print(f'| {a.clue_text:32} | {a.solution:32} | {a.challenge:2} | \n| {a.location}')

            for c in match_coordinates:
               print(f'| {c.clue_text:11} | {c.location}')

            for y in match_cryptics:
               if y.key == '-':
                  print(f'| {y.short_ver:32} | {y.location}')
               else:
                  print(f'| {y.short_ver:32} | {y.location:32} | {y.key}')

        print('')


# Create a list of AnagramClue objects and fill from file
def fill_anagram():
    file = open('anagrams.txt', 'r')
    anagrams = []

    count = 0
    for line in file:
        if count % 5 == 0:
            text = line.rstrip('\n')
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
            text = line.rstrip('\n')
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

def search(*args):
    try:
        result.set(1)
    except ValueError:
        pass

anagrams = fill_anagram()
coordinates = fill_coord()
cryptics = fill_cryptic()

# Building the UI
root = Tk()
root.title("Treasure Trails")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Dropdown label
ttk.Label(mainframe, text="Select type").grid(column=1, row=1, sticky=W)

# Type dropdown menu
types = StringVar()
type_select = ttk.Combobox(mainframe, width=8, textvariable=types)
type_select['values'] = ('Anagrams', 'Coordinates', 'Cryptics')
type_select.state(['readonly'])
type_select.grid(column=1, row=2, sticky=W)

# Search bar
search_entry = StringVar()
search_bar = ttk.Entry(mainframe, width=20, textvariable=search_entry)
search_bar.grid(column=2, row=2, sticky=W)

# Search button
ttk.Button(mainframe, text="Search", command=search).grid(column=2, row=3, sticky=E)

result = StringVar()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

search_bar.focus()
root.bind('<Return>', search)

root.mainloop()

# if __name__ == '__main__':
#     main()
