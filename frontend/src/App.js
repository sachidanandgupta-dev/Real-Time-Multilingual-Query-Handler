import React, { useState } from "react";
import { sendQuery } from "./api";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [detectedLanguage, setDetectedLanguage] = useState("");

  const handleSend = async () => {
    if (!input) return;

    setLoading(true);
    setResponse("");
    setDetectedLanguage("");
    
    try {
      const data = await sendQuery(input);
      if (data.error) {
        setResponse(`Error: ${data.error}`);
        setDetectedLanguage("");
      } else {
        setResponse(data.response);
        setDetectedLanguage(data.detected_language);
      }
    } catch (error) {
      console.error("Error:", error);
      setResponse(`Error: Failed to connect to backend. Make sure the backend server is running on http://127.0.0.1:8000`);
      setDetectedLanguage("");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && e.ctrlKey) {
      handleSend();
    }
  };

  return (
    <div className="container">
      <div className="card">
        <h1>🌍 Multilingual Query System</h1>
        <p className="subtitle">Ask questions in any language, get responses in your language</p>
        
        <div className="input-section">
          <textarea
            className="textarea"
            rows="6"
            placeholder="Type your question in any language..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={loading}
          />
          <button 
            className="button"
            onClick={handleSend}
            disabled={loading || !input}
          >
            {loading ? "Processing..." : "Send"}
          </button>
        </div>

        {detectedLanguage && (
          <div className="info">
            <strong>Detected Language:</strong> {detectedLanguage}
          </div>
        )}

        {response && (
          <div className="response-section">
            <h3>Response:</h3>
            <div className="response-box">
              {response}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;