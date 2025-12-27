import random
from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

class SorteioRequest(BaseModel):
    range_max: int
    quantidade: int

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/sortear")
async def sortear(dados: SorteioRequest):
    if dados.quantidade > dados.range_max:
        raise HTTPException(status_code=400, detail="A quantidade não pode ser maior que o range.")
    if dados.quantidade <= 0 or dados.range_max <= 0:
        raise HTTPException(status_code=400, detail="Os valores devem ser maiores que zero.")

    numeros = random.sample(range(1, dados.range_max + 1), dados.quantidade)
    numeros.sort()
    print(f"Números sorteados: {numeros}")
    
    return {"numeros": numeros}
