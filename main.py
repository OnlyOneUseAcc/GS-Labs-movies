from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import API.api_utils as ut
from asgiref.sync import sync_to_async

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
    return {
        'content': {'films': {1: {'name': 'film1',
                                  'genre': 'genre1, genre2'},
                              2: {'name': 'film2',
                                  'genre': 'genre1, genre2'},
                              3: {'name': 'film3',
                                  'genre': 'genre1, genre2'},
                              4: {'name': 'film1',
                                  'genre': 'genre1, genre2'},
                              5: {'name': 'film2',
                                  'genre': 'genre1, genre2'},
                              6: {'name': 'film3',
                                  'genre': 'genre1, genre2'},
                              7: {'name': 'film1',
                                  'genre': 'genre1, genre2'},
                              8: {'name': 'film2',
                                  'genre': 'genre1, genre2'},
                              9: {'name': 'film3',
                                  'genre': 'genre1, genre2'},
                              10: {'name': 'film1',
                                   'genre': 'genre1, genre2'},
                              11: {'name': 'film2',
                                   'genre': 'genre1, genre2'},
                              12: {'name': 'film3',
                                   'genre': 'genre1, genre2'}
                              },
                    'serials': {1: {'name': 'serial1',
                                    'genre': 'genre1, genre2'},
                                2: {'name': 'serial2',
                                    'genre': 'genre1, genre2'},
                                3: {'name': 'serial3',
                                    'genre': 'genre1, genre2'}}
                    },
        'user_id': user_id
    }


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
