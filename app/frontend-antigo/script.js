const API_URL = "http://127.0.0.1:8000";

async function analyzeText() {
  const text = document.getElementById("emailText").value;

  if (!text) {
    alert("Digite um texto antes de enviar");
    document.getElementById("emailText").value = "";
    return;
  }

  try {
    const response = await fetch(`${API_URL}/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
    const data = await response.json();
    document.getElementById("emailText").value = "";
    displayResult(data);
  } catch (error) {
    alert("Erro ao conectar com API: " + error);
  }
}

async function uploadFile() {
  const fileInput = document.getElementById("emailFile");
  if (fileInput.files.length === 0) {
    alert("Selecione um arquivo para enviar");
    return;
  }

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch(`${API_URL}/upload`, {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    displayResult(data);
  } catch (error) {
    alert("Erro ao enviar arquivo: " + error);
  }
}

function displayResult(data) {
  const resultDiv = document.getElementById("result");
  if (data.error) {
    resultDiv.innerHTML = `<p style="color:red;">Erro: ${data.error}</p>`;
  } else {
    resultDiv.innerHTML = `
            <p><strong>Categoria:</strong> ${data.categoria}</p>
            <p><strong>Texto:</strong> ${data.texto}</p>
            <p><strong>Resposta Sugerida:</strong> ${data.resposta_sugerida}</p>
        `;
  }
}
