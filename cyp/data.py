import matplotlib.pyplot as plt
import matplotlib as mpl
import requests
import pandas as pd
import re
import itertools
import string

def read_txt_file(url):
    response = requests.get(url)
    text = response.text
    return text



def remove_start(chords):
    song_list_clean_1 = []
    start_song = chords[0][:8]
    song_list_clean_1 = [song.replace(start_song, '') for song in chords]
    return song_list_clean_1


def remove_parentheses(lst):
    new_list = []
    for i in lst:
        new_list.append(re.sub(r"\([^)]*\)", "", i))
    return new_list

def remove_symbols(list_of_list):
    new_list = []
    for item in list_of_list:
        item = item.replace(':','')
        chord_list = item.split(' ')
        chord_list_clean = []
        for chord in chord_list:
            chord_list_clean.append(chord.split('/')[0])
        new_list.append(' '.join(chord_list_clean))
    return new_list

def clean_chords(chords_column):
    
    letters = list(string.ascii_uppercase)[:7]
    cleaned = []
    
    for row in chords_column:
        # Convert string to list of strings
        song_list = row.split()

        # Only chords that begin with designated letters
        raw_chords = [chord for chord in song_list if chord[0] in letters]
        
        # remove symbols
        unsymboled_chords = remove_symbols(raw_chords)
        
        # Remove repeated chords
        non_repeating_chords = []
        for idx, chord in enumerate(unsymboled_chords):
            if idx == 0:
                non_repeating_chords.append(chord)
            elif unsymboled_chords[idx - 1] != unsymboled_chords[idx]:
                non_repeating_chords.append(chord)
            else:
                pass
        
        cleaned.append(non_repeating_chords)
        
    return cleaned

def save_csv(df, filename):
    df.to_csv(filename, index=True)
    print("Dataframe saved as {}".format(filename))
