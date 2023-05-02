import numpy as np

'''
FILTER DF BY CHOOSING ONLY SONGS LONGER THAN n CHORDS
'''
def filter_length(song_len_df, min_length):
    filt_len = song_len_df['song_length'] >= min_length
    kaggle_data_v1 = song_len_df.copy()[filt_len]

    return kaggle_data_v1


'''
FILTER BY NUMBER OF SAMPLES (SONGS)
'''
def get_songs(final_df, size=5000):
    rand_list = np.random.randint(0, len(final_df), size)

    sliced_df = final_df.copy()
    sliced_df = sliced_df.drop([idx for idx in final_df.index if idx not in rand_list])

    return sliced_df
