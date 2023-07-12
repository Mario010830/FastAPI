from fastapi import FastAPI
from typing import Optional
from uuid import uuid4 as uuid
from pydantic import BaseModel

class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str
    
productos =[]    
    

app = FastAPI()

@app.get("/")
def index():
    return ("Bienvenidos a la Api de Productos")

@app.get("/productos")
def obtener_productos():
    return productos

@app.post("/productos")
def crear_producto(producto: Producto):
    producto.id = (str)(uuid())
    productos.append(producto)
    return("Producto creado satisfactoriamente")

@app.get("/productos/{producto_id}")
def obtener_producto_id(producto_id:str):
    for p in productos:
        if p.id ==producto_id:
            return p
    return(f"El producto con el id {producto_id} no fue econtrado")    