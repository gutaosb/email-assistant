import { useState } from "react";
const api_url = import.meta.env.VITE_API_URL;

const FileUpload = ({ setLoading, setResult }) => {
  const [filename, setFilename] = useState("");

  const handleUpload = async (e) => {
    const file = e.target.files[0];

    if (!file) return;

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
        <input type="file" className="hidden" onChange={handleUpload} />
      </label>
      {filename && (
        <p className="mt-2 text-gray-700">Arquivo selecionado: {filename}</p>
      )}
    </div>
  );
};

export default FileUpload;
