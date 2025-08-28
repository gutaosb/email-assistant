import { useState } from "react";
const API_URL = import.meta.env.VITE_API_URL;

const EmailForm = ({ setLoading, setResult }) => {
  const [text, setText] = useState("");

  const handleAnalyze = async () => {
    if (!text.trim()) return alert("Digite um texto primeiro");

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      alert("Erro ao conectar com API: " + err);
    }

    setLoading(false);
  };

  return (
    <div className="w-full max-w-lg mb-4">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="w-full border rounded-lg p-3 mb-2 focus:outline-none focus:ring-2 focus:ring-green-500"
        placeholder="Digite ou cole o texto do email..."
      ></textarea>

      <button
        onClick={handleAnalyze}
        className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-lg transition"
      >
        Analisar texto
      </button>
    </div>
  );
};

export default EmailForm;
