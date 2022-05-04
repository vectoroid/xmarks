import datetime
import fastapi
import hashlib
import os
import sys

app = fastapi.FastAPI()

async def get_fake_passkey():
    m = hashlib.sha3_512()
    m.update('Deta rocks! The time is now ' + datetime.datetime().now())
    return m.digest()

@app.get('/')
async def read_root():
    return {'data': {
        'message': "Hello, world!"
    }}

@app.get('diagnostix')
async def read_diagnostix():
    return {'data': {
        'deta': {
            'path': os.environ['DETA_PATH'],
            'python_version': sys.version,
            'running_on_micro': os.environ['DETA_RUNTIME'],
            'key': get_fake_passkey()
        }
    }}