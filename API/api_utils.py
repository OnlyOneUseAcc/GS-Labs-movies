import pandas as pd

DATA = 'data/'
POSTPROCESSING = 'postprocessing/'


def get_history_by_user(user_id):
    df = pd.read_csv(f'{DATA}{POSTPROCESSING}watch_history.csv', index_col=0)
    user_history = df[df['user_uid'] == user_id]

    if len(user_history) == 0:
        return []

    content = pd.read_csv(f'{DATA}{POSTPROCESSING}content.csv', index_col='content_uid')
    content_ids = user_history['content_uid'].values
    names = content.loc[content_ids, 'name'].values
    return names
