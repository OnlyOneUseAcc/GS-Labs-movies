import random
import pandas as pd
from scipy.spatial.distance import cosine
from tqdm import tqdm

from preprocessing.duration_matrix import DurationSparseMatrix

DATA = 'data/'
POSTPROCESSING = 'postprocessing/'


def get_history_by_user(user_id: int) -> list:
    df = pd.read_csv(f'{DATA}{POSTPROCESSING}watch_history.csv', index_col=0)
    content = pd.read_csv(f'{DATA}{POSTPROCESSING}content.csv', index_col='content_uid')

    user_history = df[df['user_uid'] == user_id]
    content_ids = user_history['content_uid'].values
    names = content.loc[content_ids, 'name'].values
    return names


def pipeline(id, num_similar_users):
    CONST_PATH = 'data/postprocessing/'
    user_genres = pd.read_csv(f'{CONST_PATH}users_genres.csv', index_col=0)
    user_content_type = pd.read_csv(f'{CONST_PATH}user_content_types.csv', index_col=0)
    comb_df = pd.concat([user_content_type, user_genres], axis=1)

    similarity = comb_df.drop(id, axis=0).apply(lambda row: cosine(comb_df.loc[id], row), axis=1)
    similar_users = similarity.sort_values().head(num_similar_users).index

    dsm = DurationSparseMatrix()
    history, content = dsm.read_info()
    user_films = dsm.get_matrix_part(similar_users)

    our_user = dsm.get_matrix_part([id])

    dif_films = user_films.apply(lambda row: row - our_user.iloc[0], axis=1)

    top_films = list()
    mean_dur = list()

    for col, values in dif_films.iteritems():
        genre = content.loc[col, 'type']
        for value in values:
            if value == 1:
                if col in top_films:
                    continue
                mean_dur.append(user_films[col].sum() * user_content_type.loc[id, genre])
                top_films.append(col)

    sorted_top_filmes = pd.DataFrame(data=[top_films, mean_dur]).transpose() \
                            .sort_values(by=1, ascending=False)[0].values[:50]

    return top_films
