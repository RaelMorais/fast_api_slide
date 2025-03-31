from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Exemplo de produtos fictícios
products = [
    {"product_id": 1, "name": "Smartphone", "category": "electronics", "price": 799},
    {"product_id": 2, "name": "Camiseta", "category": "clothing", "price": 29.99},
    {"product_id": 3, "name": "Laptop", "category": "electronics", "price": 1500},
    {"product_id": 4, "name": "Tênis", "category": "clothing", "price": 99.99},
]

# Endpoint para buscar produtos por nome (query parameter)
@app.get("/products")
async def search_products(name: Optional[str] = None, category: Optional[str] = None):
    """
    Busca produtos pelo nome (query parameter) e categoria (query parameter).
    - name: Nome do produto para pesquisa.
    - category: Categoria para filtrar os produtos.
    """
    # Filtrando os produtos com base no nome e categoria
    filtered_products = products
    
    if name:
        filtered_products = [product for product in filtered_products if name.lower() in product["name"].lower()]
    
    if category:
        filtered_products = [product for product in filtered_products if category.lower() in product["category"].lower()]

    return filtered_products


# Lógica:

#     A função search_products recebe dois parâmetros opcionais:

#         name: Para filtrar produtos pelo nome.

#         category: Para filtrar produtos pela categoria.

#     Primeiro, ele começa com a lista completa de produtos (filtered_products = products).

#     Se o parâmetro name for fornecido, ele filtra os produtos para incluir apenas os que contêm o texto passado no campo name (sem considerar maiúsculas ou minúsculas).

#     Se o parâmetro category for fornecido, ele filtra os produtos para incluir apenas aqueles que contêm o valor passado no campo category.

###############################################################################






# Endpoint para obter informações sobre um produto usando o ID (path parameter)
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """
    Endpoint para obter informações sobre um produto usando o ID do produto.
    O 'product_id' é um path parameter.
    """
    # Buscando o produto pelo ID
    product = next((prod for prod in products if prod["product_id"] == product_id), None)
    
    if product:
        return product
    else:
        return {"error": "Produto não encontrado"}

# Lógica:

#     Definição do Endpoint:

#         O endpoint é definido usando o decorator @app.get("/products/{product_id}").

#         O {product_id} dentro da URL indica que o valor será um path parameter. Ou seja, a URL /products/1 significa que o product_id será 1, /products/2 significa que o product_id será 2, e assim por diante.

#         Esse path parameter é passado para a função get_product como um argumento product_id do tipo int.