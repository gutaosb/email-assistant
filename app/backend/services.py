from transformers import pipeline
from utils import normalize_text

#modelo para classificacao do zero-shot do Hugging face
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

#funcao para classificacao do email:
def classify_email(text: str):
    candidate_labels = ["Produtivo", "Improdutivo"]

    try:
        result = classifier(text, candidate_labels)
        category = result['labels'][0]
        score = result['scores'][0]

        #se a confianca for baixa, usar heuristica
        if score < 0.7:
            category = heuristic_classification(text)
    except Exception:
        category = heuristic_classification(text)
    
    return category


#funcao para geracao de resposta automatica
def generate_response(text:str, category: str):
    if category == "Produtivo":
        return "Olá! Recebemos seu email e estamos analisando. Em breve daremos retorno sobre"
    else: 
        return "Obrigado pela mensagem!"
        

# fallback heuristico
def heuristic_classification(text: str):
    productive_keywords = ["reuniao", "projeto", "prazo", "relatorio", "entrega", "solicitacao", "urgente", "confirmacao"]
    normalized_text = normalize_text(text)

    return "Produtivo" if any(word in normalized_text for word in productive_keywords) else "Improdutivo"
