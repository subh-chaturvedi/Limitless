import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [question, setQuestion] = useState('');
  const [followupQuestions, setFollowupQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [response, setResponse] = useState('');

  const handleQuestionSubmit = async () => {
    try {
      const res = await axios.post('http://localhost:5000/ask', { question });
      setFollowupQuestions(res.data.followup_questions);
    } catch (error) {
      console.error("There was an error submitting the question!", error);
    }
  };

  const handleAnswerChange = (index, value) => {
    setAnswers(prev => ({ ...prev, [index]: value }));
  };

  const handleAnswersSubmit = async () => {
    try {
      const res = await axios.post('http://localhost:5000/submit_answers', { answers });
      setResponse(res.data.response);
    } catch (error) {
      console.error("There was an error submitting the answers!", error);
    }
  };

  return (
    <div className="App">
      <h1>Ask a Question</h1>
      <input 
        type="text" 
        value={question} 
        onChange={e => setQuestion(e.target.value)} 
      />
      <button onClick={handleQuestionSubmit}>Submit</button>

      {followupQuestions.map((q, index) => (
        <div key={index}>
          <h2>{q}</h2>
          <input 
            type="text" 
            onChange={e => handleAnswerChange(index, e.target.value)} 
          />
        </div>
      ))}

      {followupQuestions.length > 0 && (
        <button onClick={handleAnswersSubmit}>Submit Answers</button>
      )}

      {response && <h2>{response}</h2>}
    </div>
  );
}

export default App;
