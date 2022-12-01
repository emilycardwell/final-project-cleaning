




def csv_to_concat_df(csv_1, csv_2):
    df_1 = pd.read_csv(csv_1)
    df_2 = pd.read_csv(csv_2)
    return pd.concat([df_1, df_2], axis=0)




def count_chords(cleaned_df):

    chord_count_df = pd.DataFrame()
    chords_count_dict = {}
    
    for song in cleaned_df['chords']:
        song_dict = dict(Counter(song))
        for chord, count in song_dict.items():
            if chord in chords_count_dict:
                chords_count_dict[chord] = chords_count_dict[chord] + count
            else:
                chords_count_dict[chord] = count
                
    return chords_count_dict



def data_slicer(data_frame, word):
    return data_frame[data_frame['genres'].str.contains(word, case=False)]


def check_most_frequent(df, chord):

    # get the column of df with the chord provided as input
    df_chord = df['chords']

    # create a list of all the elements in the chord column
    chords_list = df_chord.tolist()

    # count the frequency of each element in the list
    chords_count = {}
    for chord in chords_list:
        if chord in chords_count:
            chords_count[chord] += 1
        else:
            chords_count[chord] = 1

  # sort the frequencies in descending order
  sorted_chords_count = {k: v for k, v in sorted(chords_count.items(), key=lambda item: item[1], reverse=True)}

  # get the most frequent element
  most_frequent = list(sorted_chords_count.keys())[0]

    return most_frequent
