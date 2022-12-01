
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
