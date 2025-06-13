from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def raiz():
    return {"Hello": "World"}

@app.get("/msg")
async def mensagem():
    return {"Mensagem": "Este é um exemplo de mensagem"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)
    

    