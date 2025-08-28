from utils import normalize_text
import requests
import os

#Pegando token da hugging face do .env
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

#funcao para classificacao do email:
def classify_email(text: str): 

    candidate_labels = ["Produtivo", "Improdutivo"] 
    try:
        payload = {"inputs": text, "parameters": {"candidate_labels": candidate_labels}}
        response = requests.post(
            HF_API_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            category = result['labels'][0]
            score = result['scores'][0]

        #se a confianca for baixa, usar heuristica
        if score < 0.7:
            category = heuristic_classification(text)
        #se a api falhar, usar heuristica
        else:
            return heuristic_classification(text)

    except Exception:
        category = heuristic_classification(text)
    
    return category
    
    


#funcao para geracao de resposta automatica
def generate_response(category: str):
    if category == "Produtivo": 
        return "Olá! Recebemos seu email e estamos analisando. Em breve daremos retorno sobre" 
    else: 
        return "Obrigado pela mensagem!"
        

# fallback heuristico
def heuristic_classification(text: str):
    productive_keywords = [
        "reuniao", "projeto", "prazo", "relatorio",
        "entrega", "solicitacao", "urgente", "confirmacao"
    ]
    normalized_text = normalize_text(text)

    return "Produtivo" if any(word in normalized_text for word in productive_keywords) else "Improdutivo"
