import { useState } from 'react';

const initialForm = {
  study_hours_per_day: '',
  deep_work_sessions: '',
  assignment_completion_rate: '',
  attendance_percentage: '',
  social_media_hours: '',
  gaming_hours: '',
  stress_level: '',
  motivation_level: '',
  focus_score: '',
  procrastination_index: '',
  mental_state: 'Focused',
  sleep_hours: '',
  financial_stress: '',
  revision_efficiency: '',
  burnout_risk: '',
  consistency_score: ''
};

const fieldLabels = {
  study_hours_per_day: 'Study Hours Per Day',
  deep_work_sessions: 'Deep Work Sessions',
  assignment_completion_rate: 'Assignment Completion Rate',
  attendance_percentage: 'Attendance Percentage',
  social_media_hours: 'Social Media Hours',
  gaming_hours: 'Gaming Hours',
  stress_level: 'Stress Level',
  motivation_level: 'Motivation Level',
  focus_score: 'Focus Score',
  procrastination_index: 'Procrastination Index',
  mental_state: 'Mental State',
  sleep_hours: 'Sleep Hours',
  financial_stress: 'Financial Stress',
  revision_efficiency: 'Revision Efficiency',
  burnout_risk: 'Burnout Risk',
  consistency_score: 'Consistency Score'
};

const numericFields = [
  'study_hours_per_day',
  'deep_work_sessions',
  'assignment_completion_rate',
  'attendance_percentage',
  'social_media_hours',
  'gaming_hours',
  'stress_level',
  'motivation_level',
  'focus_score',
  'procrastination_index',
  'sleep_hours',
  'financial_stress',
  'revision_efficiency',
  'burnout_risk',
  'consistency_score'
];

const sliderFields = new Set([
  'stress_level',
  'motivation_level',
  'focus_score',
  'procrastination_index',
  'sleep_hours',
  'financial_stress',
  'revision_efficiency',
  'burnout_risk',
  'consistency_score'
]);

function App() {
  const [formData, setFormData] = useState(initialForm);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((current) => ({
      ...current,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    setPrediction(null);

    try {
      const payload = {
        ...formData,
        ...Object.fromEntries(
          numericFields.map((field) => [field, Number(formData[field])])
        ),
        deep_work_sessions: Number(formData.deep_work_sessions),
        mental_state: formData.mental_state
      };
      const backendBase = import.meta.env.VITE_BACKEND_URL;

      if (!backendBase) {
        throw new Error('VITE_BACKEND_URL is not set');
      }

      const response = await fetch(`${backendBase}/api/predict/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        const message = await response.text();
        throw new Error(message || 'Request failed');
      }

      const data = await response.json();
      setPrediction(data.prediction);
    } catch (requestError) {
      setError('Could not get prediction. Check that the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFormData(initialForm);
    setPrediction(null);
    setError('');
  };

  return (
    <div className="page-shell">
      <div className="backdrop backdrop-one" />
      <div className="backdrop backdrop-two" />

      <main className="app-card">
        <section className="hero">
          <p className="eyebrow">Student Performance Predictor</p>
          <h1>Predict final exam score from student behavior data.</h1>
          <p className="subtitle">
            Enter study habits, focus, stress, and lifestyle values, then send them to the backend model.
          </p>
        </section>

        <form className="predict-form" onSubmit={handleSubmit}>
          <div className="grid">
            {numericFields.map((field) => (
              <label className="field" key={field}>
                <span className="field-head">
                  <span>{fieldLabels[field]}</span>
                  {sliderFields.has(field) ? <span className="field-value">{formData[field] || 0}/10</span> : null}
                </span>
                {sliderFields.has(field) ? (
                  <input
                    type="range"
                    name={field}
                    value={formData[field]}
                    onChange={handleChange}
                    min="0"
                    max="10"
                    step="1"
                    required
                  />
                ) : (
                  <input
                    type="number"
                    name={field}
                    value={formData[field]}
                    onChange={handleChange}
                    step="any"
                    required
                  />
                )}
              </label>
            ))}

            <label className="field field-full">
              <span>{fieldLabels.mental_state}</span>
              <select name="mental_state" value={formData.mental_state} onChange={handleChange}>
                <option value="Focused">Focused</option>
                <option value="Distracted">Distracted</option>
                <option value="Burnout">Burnout</option>
                <option value="Balanced">Balanced</option>
              </select>
            </label>
          </div>

          <div className="actions">
            <button className="primary-btn" type="submit" disabled={loading}>
              {loading ? 'Predicting...' : 'Predict Score'}
            </button>
            <button className="secondary-btn" type="button" onClick={handleReset}>
              Reset
            </button>
          </div>
        </form>

        {error ? <div className="message error">{error}</div> : null}

        {prediction !== null ? (
          <div className="message result">
            Predicted Final Exam Score: <strong>{Number(prediction).toFixed(2)}</strong>
          </div>
        ) : null}
      </main>
    </div>
  );
}

export default App;
