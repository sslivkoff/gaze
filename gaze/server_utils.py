import fastapi
import uvicorn


app = fastapi.FastAPI()


@app.get("/")
def home():
    return {"message": "hello world"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000)

