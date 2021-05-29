from fastapi import FastAPI

app = FastAPI()


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
