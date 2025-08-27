import { useState } from "react";
import EmailForm from "./components/EmailForm";
import FileUpload from "./components/FileUpload";
import ResultCard from "./components/ResultCard";
import Loader from "./components/Loader";

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen flex flex-col items-center justify-start bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">
        Analisando emails ✉️
      </h1>

      <EmailForm setLoading={setLoading} setResult={setResult} />
      <FileUpload setLoading={setLoading} setResult={setResult} />

      {loading && <Loader />}
      {result && <ResultCard result={result} />}
    </div>
  );
}

export default App;
