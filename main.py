from fastapi import FastAPI,status

app= FastAPI()

@app.get('/')
def get_status():
    return {
        'message': 'server is up and running',
        'status': status.HTTP_200_OK
    }