import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
async def index():
    return {"message": "hello"}



def run_server(host="0.0.0.0", port=8000):
    print(f"Running the API on http://{host}:{port}/ !")
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
    )

