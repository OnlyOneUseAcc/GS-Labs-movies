from fastapi import FastAPI

app = FastAPI()


@app.get("/user_recomendation")
async def predict(user_id: int):
    return {'content': {'films': {1: 'film1',
                                  2: 'film2',
                                  3: 'film3'},
                        'serials': {1: 'serial1',
                                    2: 'serial2',
                                    3: 'serial3'}
                        },
            'user_id': user_id
            }
