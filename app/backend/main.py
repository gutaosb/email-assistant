#criacao API
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from services import classify_email, generate_response
from utils import read_file
import logging
import os
import uvicorn

# configuracao de logs
logging.basicConfig(level=logging.INFO)


app = FastAPI()


# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#modelo para receber o texto
class EmailInput(BaseModel):
    text:str


#Rotas da API -------------------------------

@app.get('/api')
def read_root():
    return({"message":"server rodando"})

@app.post('/api/analyze')
def analyze_email(email: EmailInput):

    try:
        #validacao de entrada
        if not email.text or email.text.strip() == "":
            return JSONResponse(
                status_code=400,
                content={"erro": "O texto nao pode ser vazio"}
            )
        
        #classificacao
        category = classify_email(email.text)    
        response_text = generate_response(email.text, category)

        return JSONResponse(
            status_code=200,
            content={
                "categoria": category,
                "texto": email.text,
                "resposta_sugerida": response_text,
            }
        )

    except Exception as e:
        logging.error(f"Erro no /analyze: {e}")
        return JSONResponse(
            status_code=500,
            content={"erro": f"Ocorreu um erro interno: {str(e)}"}
        )



@app.post('/api/upload')
async def upload_file(file: UploadFile = File(...)):
    try:
        #validar extensao do arquivo
        if not file.filename.endswith((".txt", ".pdf")):
            return JSONResponse(
                status_code=415,
                content={"erro": "Formato de arquivo nao suportado, apenas .txt ou .pdf"}
            )
        
        #ler conteudo do arquivo
        content = await read_file(file)

        #classificacao
        category = classify_email(content)
        response_text = generate_response(content, category)

        return JSONResponse(
            status_code=200,
            content={
                "categoria": category, 
                "texto": content, 
                "resposta_sugerida": response_text
                }
            
            )
    except Exception as e:
        logging.error(f"Erro no /upload: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"erro": f"Ocorreu um erro interno: {str(e)}"}
        )



#Servir frontend -----------------------------

# Configura frontend React (build)
app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    file_path = os.path.join("dist", full_path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse("dist/index.html")


# # Ponto de entrada
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 8000))  # Render fornece a porta via env
#     uvicorn.run("app.backend.main:app", host="0.0.0.0", port=port, reload=False)