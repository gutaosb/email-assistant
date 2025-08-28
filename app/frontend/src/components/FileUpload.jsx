import { useState } from "react";
const api_url = import.meta.env.VITE_API_URL;

const FileUpload = ({ setLoading, setResult }) => {
  const [filename, setFilename] = useState("");

  const handleUpload = async (e) => {
    const file = e.target.files[0];

    if (!file) return;

    // valida extensão do arquivo
    const validExtensions = [".txt", ".pdf"];
    const fileExtension = file.name
      .slice(file.name.lastIndexOf("."))
      .toLowerCase();

    if (!validExtensions.includes(fileExtension)) {
      alert(
        "Formato do arquivo não suportado. Apenas .txt e .pdf são aceitos."
      );
      e.target.value = ""; // limpa o input
      return;
    }

    setFilename(file.name);
    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(`${api_url}/upload`, {
        method: "POST",
        body: formData,
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
      <label className="w-full cursor-pointer bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg inline-block text-center transition">
        📂 Escolher Arquivo
        <input
          type="file"
          className="hidden"
          onChange={handleUpload}
          accept=".txt,.pdf"
        />
      </label>
      {filename && (
        <p className="mt-2 text-gray-700">Arquivo selecionado: {filename}</p>
      )}
    </div>
  );
};

export default FileUpload;
