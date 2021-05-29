from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import API.api_utils as ut
import json
from typing import Set


class WatchHistory(BaseModel):
    films: Set[str] = None


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
                                  'genre': 'genre1, genre2'}},
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


@app.get('/watch_history', response_model=WatchHistory)
async def history(user_id):
    user_history = ut.get_history_by_user(user_id)
    model = WatchHistory()
    model.films = list(user_history)
    return model
