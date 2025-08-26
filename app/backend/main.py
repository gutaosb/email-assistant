#criacao API
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from services import classify_email, generate_response
from utils import read_file


app = FastAPI()

#modelo para receber o texto
class EmailInput(BaseModel):
    text:str


@app.get('/')
def read_root():
    return({"message":"server rodando"})

@app.post('/analyze')
def analyze_email(email: EmailInput):

    try:
        category = classify_email(email.text)    
        response_text = generate_response(email.text, category)

        return {"categoria": category, "texto": email.text, "resposta_sugerida": response_text}

    except Exception as e:
        return({"erro": str(e)})


@app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await read_file(file)
        category = classify_email(content)
        response_text = generate_response(content, category)
        return {"categoria": category, "texto": content, "resposta_sugerida": response_text}
    except Exception as e:
        return {"error": str(e)}

    