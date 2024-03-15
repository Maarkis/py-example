from fastapi import FastAPI
import uvicorn


app = FastAPI(title="Example", version="1.0.0")

if __name__ == "__main__":
    config = uvicorn.Config("main:app", reload=True, port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
