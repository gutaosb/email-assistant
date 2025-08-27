const ResultCard = ({ result }) => {
  return (
    <div className="mt-6 bg-white shadow-md border rounded-lg p-4 w-full max-w-lg">
      <p>
        <strong>Categoria:</strong> {result.categoria}
      </p>

      <p className="mt-2">
        <strong>Texto do email:</strong>
      </p>
      <div className="mt-1 p-2 bg-gray-50 rounded">{result.texto}</div>

      <p className="mt-2">
        <strong>Resposta sugerida:</strong>
      </p>
      <div className="mt-1 p-2 bg-gray-50 rounded">
        {result.resposta_sugerida}
      </div>
    </div>
  );
};

export default ResultCard;
