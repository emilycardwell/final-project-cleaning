import pandas as pd
from collections import Counter
import os
import seaborn as sns
import matplotlib.pyplot as plt

'''
Get DATA
'''
def get_csv_data(file_name):
    data_path = os.path.join('~/code/emilycardwell/final-project-data/data/raw', file_name)
    raw_csv_df = pd.read_csv(data_path)
    return raw_csv_df

def get_text_data(file_name):
    data_path = os.path.join('~/code/emilycardwell/final-project-data/data/raw', file_name)
    raw_txt_df = pd.read_csv(data_path, sep="_START_|_END_", header=None, engine='python').T
    return raw_txt_df

'''
GET CHORD COUNT & OPTIONAL DISTRIBUTION
'''
def count_chords(file_name, low_freq_to_remove=10, histplot=False, ascending=False):
    data_path = os.path.join('~/code/emilycardwell/final-project-data/data/clean', file_name)
    cleaned_csv_df = pd.read_csv(data_path)

    chords_count_dict = {}
    for song in cleaned_csv_df['chords']:
        song_dict = dict(Counter(song))
        for chord, count in song_dict.items():
            if chord in chords_count_dict:
                chords_count_dict[chord] = chords_count_dict[chord] + count
            else:
                chords_count_dict[chord] = count

    slim_chord_counts_dict = {}
    for chord, count in chords_count_dict.items():
        if count <= low_freq_to_remove:
            pass
        else:
            slim_chord_counts_dict[chord] = count

    chord_count_df = pd.Series(slim_chord_counts_dict).to_frame('chord_count')
    chord_count_df.sort_values(by='chord_count', ascending=ascending, inplace=True)

    if histplot == True:
        print()
        chords_fig = sns.barplot(chord_count_df)
        chords_fig.set_xlabel('chord')
        plt.show()
    else:
        pass

    return chord_count_df


'''
GET GENRE DISTRIBUTION
'''
def count_genres(final_df, histplot=False):

    genre_count_ser = final_df['genres'].value_counts()

    genre_count_df = genre_count_ser.to_frame('genre_count')

    genre_count_df.sort_values(by='genre_count', ascending=False, inplace=True)

    if histplot == True:
        genres_fig = sns.histplot(genre_count_df, bins=100)
        genres_fig.set(xticklabels=[])
        genres_fig.set_xlabel('genres')
        plt.show()
    else:
        pass

    return genre_count_df


'''
GET ARTIST DISTRIBUTION
'''
def count_artists(final_df, histplot=False):

    artist_count_ser = final_df['artist_name'].value_counts()

    artist_count_df = artist_count_ser.to_frame('artist_count')

    artist_count_df.sort_values(by='artist_count', ascending=False, inplace=True)

    if histplot == True:
        artists_fig = sns.histplot(final_df['artist_name'], bins=100)
        artists_fig.set(xticklabels=[])
        artists_fig.set_xlabel('artists')
        plt.show()
    return artist_count_df


'''
SEND CLEAN DF TO CVS
'''
def df_to_csv(final_df, version, save_path):

    filename = 'final_df' + '_v' + version + '.csv'
    # how do i get an object to the a string of it's name?
    my_path = os.path.join(save_path, filename)

    final_df.to_csv(my_path)

    return print(f'{filename} saved to {save_path}')
