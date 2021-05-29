import pandas as pd

DATA = 'data/'
POSTPROCESSING = 'postprocessing/'


def get_history_by_user(user_id: int) -> list:
    df = pd.read_csv(f'{DATA}{POSTPROCESSING}watch_history.csv', index_col=0)
    content = pd.read_csv(f'{DATA}{POSTPROCESSING}content.csv', index_col='content_uid')

    user_history = df[df['user_uid'] == int(user_id)]
    content_ids = user_history['content_uid'].values
    names = content.loc[content_ids, 'name'].values
    return names
