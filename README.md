```python -m venv _env```
 Criar a venv 

 ```.\_env\Scripts\activate```
 Ativar a venv 

 ```pip install fastapi uvicorn```
 Instalar Fast e Uvicorn 

 ```uvicorn nome_do_arquivo:app --reload```
 Rodar o código 

 ``http://127.0.0.1:8000/products/1``

Teste de Path parameters

```http://127.0.0.1:8000/products?name=Smartphone```

Teste de Query paremeters