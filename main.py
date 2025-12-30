from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SiteRequest(BaseModel):
    nome: str
    tipo: str
    cidade: str
    servicos: str

@app.post("/criar-site")
def criar_site(data: SiteRequest):
    prompt = f"""
Cria um website profissional completo em HTML e CSS para o seguinte negócio:

Nome da empresa: {data.nome}
Tipo de negócio: {data.tipo}
Cidade: {data.cidade}
Serviços: {data.servicos}

Requisitos:
- Português de Portugal
- Design moderno
- Mobile-first
- Estrutura completa
- SEO básico
- Inclui header, hero, serviços, sobre, contactos
- Gera APENAS código HTML + CSS
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    html_code = response.choices[0].message.content

    return {
        "html": html_code,
        "preview": "https://preview-cliente.netlify.app"
    }
