from fastapi import FastAPI, HTTPException
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
    result =list(filter(lambda p:p.id==producto_id, productos))
    if len(result):
        return result[0]
    raise HTTPException(status_code=404, detail="Producto no encontrado")