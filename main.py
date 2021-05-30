from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import API.api_utils as ut
from asgiref.sync import sync_to_async
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/user_recommendation")
async def predict(user_id: int):
    result = {'content': {},
              'user_id': user_id}
    film_ids = ut.pipeline(user_id, 2000)

    content = pd.read_csv('data/postprocessing/content.csv', index_col='content_uid')
    content = content.loc[film_ids]
    for index, row in content.iterrows():
        result['content'][index] = {}
        result['content'][index]['name'] = row['name']
        result['content'][index]['genre'] = row['genres']
        if type(result['content'][index]['genre']) == float:
            result['content'][index]['genre'] = '-'

    return result


@app.get('/exist_user')
async def is_exist(user_id: int):
    return {
        'content': {
            'exist': True
        }}


@app.get('/top_films_per_genre')
async def top_films(user_id: int):
    return {
        'content': {
            'genre1': {
                1: {'name': 'serial1',
                    'type': 'serial'
                    },
                2: {'name': 'film1',
                    'type': 'film'}
            },
            'genre2': {
                1: {'name': 'serial2',
                    'type': 'serial'
                    },
                2: {'name': 'film2',
                    'type': 'film'}
            }
        }
    }


@app.get('/watch_history')
async def history(user_id: int):
    user_history = {'content': {}}
    for i, name in enumerate(await sync_to_async(ut.get_history_by_user)(int(user_id))):
        user_history['content'][i] = name
    return user_history
