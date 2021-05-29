from fastapi import FastAPI

app = FastAPI()


@app.get("/user_recomendation")
async def predict(user_id: int):
    return {'content': {'films': {1: {'name': 'film1',
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
