import unicodedata
import PyPDF2
from fastapi import UploadFile

#ler arquivo .txt ou .pdf
async def read_file(file: UploadFile):
    content = ""

    if file.filename.endswith(".txt"):
        content = (await file.read()).decode("utf-8")
    elif file.filename.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file.file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                content += page_text + "\n"
    else:
        raise ValueError("Formato não suportado. Use .txt ou .pdf")
    return content


#normalizando textos
def normalize_text(text):
    norm_text = unicodedata.normalize("NFD", text)
    correct_text = "".join([c for c in norm_text if unicodedata.category(c) != "Mn"]).lower()

    return correct_text