from fastapi import FastAPI
from typing import Union

from Models.items_model import Item


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

@app.put("/items/{item_id}")
def update_item(item_id:int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "item_price": item.price}
