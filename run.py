import uvicorn


def server():
    uvicorn.run("server:app", port=8000, reload=True)


if __name__ == "__main__":
    server()
