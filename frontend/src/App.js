import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [code, setCode] = useState("");
  const [summary, setSummary] = useState("");
  const [bugs, setBugs] = useState("");
  const [fixed, setFixed] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRequest = async (type) => {
    setLoading(true);

    try {
      let url = "";

      if (type === "summarize") url = "http://127.0.0.1:8000/summarize";
      if (type === "detect") url = "http://127.0.0.1:8000/detect-bug";
      if (type === "fix") url = "http://127.0.0.1:8000/fix-code";

      const res = await axios.post(url, { code });

      if (type === "summarize") setSummary(res.data.summary);
      if (type === "detect") setBugs(res.data.issues);
      if (type === "fix") setFixed(res.data.fixed_code);
    } catch (err) {
      alert("Error connecting to backend!");
    }

    setLoading(false);
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    alert("Copied!");
  };

  const clearAll = () => {
    setCode("");
    setSummary("");
    setBugs("");
    setFixed("");
  };

  return (
    <div className="container">
      <h1>💻 Smart Code Fixer</h1>

      <textarea
        className="code-box"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your Python code here..."
      />

      <div className="button-group">
        <button onClick={() => handleRequest("summarize")} className="btn blue">
          Summarize
        </button>
        <button onClick={() => handleRequest("detect")} className="btn red">
          Detect Bug
        </button>
        <button onClick={() => handleRequest("fix")} className="btn green">
          Fix Code
        </button>
        <button onClick={clearAll} className="btn gray">
          Clear
        </button>
      </div>

      {loading && <p className="loading">⏳ Processing...</p>}

      <div className="output">
        <div className="card">
          <h3>Summary</h3>
          <pre>{summary}</pre>
          {summary && (
            <button onClick={() => copyToClipboard(summary)}>Copy</button>
          )}
        </div>

        <div className="card">
          <h3>Detected Bugs</h3>
          <pre>{bugs}</pre>
          {bugs && (
            <button onClick={() => copyToClipboard(bugs)}>Copy</button>
          )}
        </div>

        <div className="card">
          <h3>Fixed Code</h3>
          <pre>{fixed}</pre>
          {fixed && (
            <button onClick={() => copyToClipboard(fixed)}>Copy</button>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;