from fastapi import FastAPI
from typing import Union

#Creacion de una aplicacion FastAPI basica:
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/hola")
def holaMundo():
    return {"Hola Mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id":item_id,"q" : q}     

@app.get("/calculadora")
def calcular(operando_1: float, operando_2:float):
    return {"suma":operando_1 + operando_2}