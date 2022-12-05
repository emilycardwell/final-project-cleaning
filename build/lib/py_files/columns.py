import numpy as np

'''
TURN SINGLE CHORDS COLUMN TO DATAFRAME TO CONCAT
'''
def expand_cols(raw_txt_df):
    raw_txt_df.rename(columns={0: "chords"}, inplace=True)
    raw_txt_df.replace(' ', np.nan, inplace=True)
    raw_txt_df.dropna(inplace=True)
    raw_txt_df.insert(0, 'artist_name', 'unknown', True)
    raw_txt_df.insert(0, 'genres', 'jazz', True)
    raw_txt_df['song_name'] = 'unknown'
    return raw_txt_df

'''
DROP DUPLICATES BASED ON SONG & ARTIST TITLES
DROP UNWANTED COLUMNS
'''
def drop_dups_cols(raw_df):

    nonrepeated_songs_df = raw_df.drop_duplicates(
                                subset=['artist_name', 'song_name'],
                                keep = 'first').reset_index(drop = True)

    slim_df = nonrepeated_songs_df.loc[:, ['artist_name', 'genres',
                                           'chords', 'song_name']]
    return slim_df


'''
CONCAT CHORDS INTO ONE LONG STRING PER SONG
MAKE SONG TITLES ALL CAPS
'''
def new_columns(cleaned_df):
    new_columns_df = cleaned_df.copy()

    new_columns_df['chords_list'] = \
        [''.join(map(str, l)) for l in new_columns_df['chords']]
    new_columns_df['song_name'] = \
        [name.upper() for name in new_columns_df['song_name']]

    return new_columns_df

def song_length(clean_genres_df):
    song_len_df = clean_genres_df.copy()
    # new column
    song_len_df['song_length'] = 0

    for index in song_len_df.index:
        song_len_df.loc[index, 'song_length'] = len(song_len_df.loc[index, 'chords'])

    return song_len_df
