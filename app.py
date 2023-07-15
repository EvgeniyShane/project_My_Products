from fastapi import FastAPI, HTTPException
from models.product import Product
import sqlite3
app = FastAPI()

def mappingProduct(products: list):
    result = []
    for product in products:
        result.append(Product(product[0], product[1], product[2]))
    return result

@app.get("/products")
async def get_products():
    products = []
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, price FROM products")
        products = cursor.fetchall()
    return mappingProduct(products)

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product = None
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, price FROM products WHERE id=?", (product_id,))
        product = cursor.fetchone()
    return Product(product[0], product[1], product[2])

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET title=?, price=? WHERE id=?", (product.title, product.price, product_id))
        connection.commit()
    return Product(product_id, product.title, product.price)

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    with sqlite3.connect("eshop.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        connection.commit()
    return {"message": "Deleted"}

