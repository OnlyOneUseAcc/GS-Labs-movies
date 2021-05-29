from fastapi import FastAPI

app = FastAPI()


@app.get("/user_recomendation")
async def predict(user_id: int):
    return {'content': {'films': {['name1', 'name2', 'name3']},
                        'serials': {['serial1', 'serial2', 'serial3']}
                        },
            'user_id': user_id
            }
