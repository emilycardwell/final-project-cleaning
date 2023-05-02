'''
GET GENRES COLUMN FOR JAZZ DATAFRAME
'''


'''
TRANSLATE MULTIPLE SUBGENRES TO MAIN GENRES (FOR MOST)
'''
def genre_cleaning(genres_column):
    # most common genres list
    popular_genres = ['pop', 'rock', 'jazz', 'folk', 'blues', 'country', 'world',
                    'sertanejo', 'adoracao', 'rock-and-roll', 'bossa nova', 'reggae',
                    'lounge', 'metal', 'pagode', 'latin worship', 'mpb']

    cleaned_genres = genres_column.copy()

    # replace lists of subgenres with main genre (in most but not all)
    for idx, element in enumerate(cleaned_genres):
        for genre in popular_genres:
            if genre in element:
                cleaned_genres[idx] = genre
            else:
                pass

    # change empty genres to 'unknown'
    for idx, element in enumerate(cleaned_genres):
        if element == '[]':
            cleaned_genres[idx] = 'unknown'
        else:
            pass

    return cleaned_genres
