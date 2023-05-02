import string
import re
from itertools import groupby


'''
REPLACE USEFUL SYMBOLS WITH STRINGS
DELETE USELESS SYMBOLS (BREAK OR JUST DELETIONS)
'''
def dashes_commas_colons(song):
    # Fix dashes, colons, and commas
    for idx, chord in enumerate(song):
        if '--' in chord:
            song[idx] = chord.split('--')[0]
        elif '-' in chord:
            linechords = chord.split('-')
            song[idx] = linechords[0]
            i = idx + 1
            for lc in linechords[1:]:
                song.insert(i, lc)
                i += 1
        elif ',' in chord:
            linechords = chord.split(',')
            song[idx] = linechords[0]
            i = idx + 1
            for lc in linechords[1:]:
                song.insert(i, lc)
                i += 1

    return song

def slashes(song):
    # Break all slash chords
    for idx, chord in enumerate(song):
        if '/' in chord:
            song[idx] = chord.split('/')[0]
        elif '|' in chord:
            song[idx] = chord.split('|')[0]
        elif '\\' in chord:
            song[idx] = chord.split('\\')[0]

    return song

def translations(song):
    # Translate uselful symbols to string
    useful_symbols = {'*': 'dim', '°': 'dim', 'º': 'dim', 'o': 'dim',
                      '+': 'aug', '#': 'sharp', ':': '', 'flat': 'b'}

    for idx, chord in enumerate(song):
        for sym in useful_symbols:
            if sym in chord:
                song[idx] = chord.replace(sym, useful_symbols[sym])

    return song

def punctuation(song):

    cleaned_song = song.copy()

    cleaned_song = dashes_commas_colons(cleaned_song)

    cleaned_song = slashes(cleaned_song)

    cleaned_song = translations(cleaned_song)

    # delete all other symbols
    for idx, chord in enumerate(cleaned_song):
        cleaned_song[idx] = re.sub(r'[^\w\s]', '', chord)

    #translate sharps back into symbols
    for idx, chord in enumerate(cleaned_song):
        if 'sharp' in cleaned_song[idx]:
            cleaned_song[idx] = chord.replace('sharp', '#')

    return cleaned_song

'''
MERGE CHORDS INTO SINGLE FORMAT
DELETE NON-CHORDS (WORDS)
'''
def merge_chords(song):
    # dictionary of correct formats (keys) and incorrect (values)
    chords_format = {'M7': ['major7', 'maj7', '7M', 'Major7', 'Maj7'],
                     'm7': ['minor7', 'min7'],
                     'hdim7': ['h7', 'hdim', 'hdim7', 'h'],
                     '7': ['sus', '9', '11', '13'],
                     'aug': ['augmented'],
                     'm': ['minor', 'min'],
                     'dim': ['diminished'],
                     '': ['add', 'major', 'maj', 'M', 'Major', 'Maj', '2', '4', '6'],
                     }

    merged_song = song.copy()

    # substitute correct formats
    for key, value in chords_format.items():
        for i in value:
            for idx, chord in enumerate(merged_song):
                if i in chord:
                    merged_song[idx] = chord.split(i)[0] + key

    # delete words (based on second letter)
    for idx, chord in enumerate(merged_song):
        if len(chord) > 1:
            if chord[1] != '#' or chord[1] != 'b':
                if chord[1:] not in chords_format.keys():
                    del merged_song[idx]
            elif chord[1] == '#' or chord[1] == 'b':
                if chord[2:] not in chords_format.keys():
                    del merged_song[idx]

    return merged_song

'''
*PARENT FUNCTION*
CONVERT STRINGS TO LISTS OF STRINGS
FILTER CHORDS BY ALLOWABLE FIRST LETTER
DELETE SPECIAL WORDS
SEND TO PUNCTUATION AND MERGE
REMOVE CONSECUTIVELY REPEATING CHORDS
DELETE EMPTY CHORDS
DELETE STAND-ALONE NUMBERS
'''
def clean_chords(chords_column):

    letters = list(string.ascii_uppercase)[:7]
    cleaned = []

    column = chords_column.copy()

    for row in column:
        # Convert string to list of strings
        if type(row) is str:
            song_list = row.split()
        else:
            print('error: data in row not string;', f'{type(row)}')

        # Only chords that begin with designated letters
        raw_chords = [chord for chord in song_list if chord[0] in letters]

        # Delete 'chords' and 'chorus'
        for idx, chord in enumerate(raw_chords):
            if 'chor' in chord.lower() or 'bass' in chord.lower():
                del raw_chords[idx]

        # remove symbols
        unsymboled_chords = punctuation(raw_chords)

        # merge chords into same format
        merged_chords = merge_chords(unsymboled_chords)

        # Remove repeated chords
        non_repeating_chords = [c[0] for c in groupby(merged_chords)]

        # Delete empty strings and numbers
        clean_song = [chord for chord in non_repeating_chords if len(chord) > 0]
        clean_song = [chord for chord in clean_song if chord[0] in letters]

        cleaned.append(clean_song)

    return cleaned
