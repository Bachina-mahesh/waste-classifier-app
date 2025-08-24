import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [wasteDetected, setWasteDetected] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setWasteDetected([]); // Clear previous results
    setError(null); // Clear previous errors
  };

  const handleAnalyze = async () => {
    if (!file) {
      setError('Please select an image first.');
      return;
    }

    setLoading(true);
    setError(null);
    setWasteDetected([]);

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await fetch('http://localhost:5001/predict', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Prediction failed.');
      }

      const data = await response.json();
      
      // ✅ CORRECTLY UPDATE THE STATE WITH THE RECEIVED DATA
      setWasteDetected(data.waste_detected);
      
    } catch (err) {
      setError(`Prediction failed: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Waste Detector</h1>
      <div className="input-section">
        <input type="file" onChange={handleFileChange} accept="image/*" />
        <button onClick={handleAnalyze} disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze Image'}
        </button>
      </div>

      {/* ✅ CONDITIONAL RENDERING FOR OUTPUT */}
      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}

      {wasteDetected.length > 0 && (
        <div className="results-container">
          <h2>Detected Waste:</h2>
          {wasteDetected.map((item, index) => (
            <div key={index} className="waste-item">
              <h3>Type: {item.type}</h3>
              <p><strong>Decomposition Time:</strong> {item.decomposition}</p>
              <p><strong>Tips:</strong> {item.tip}</p>
              <p><strong>Disposal:</strong> {item.disposal}</p>
            </div>
          ))}
        </div>
      )}

      {/* Optional: Message for no confident predictions */}
      {wasteDetected.length === 0 && !loading && !error && file && (
        <p>No waste types were confidently detected. Please try a different image.</p>
      )}
    </div>
  );
}

export default App;