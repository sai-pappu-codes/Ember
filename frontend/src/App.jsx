import { useState, useEffect } from 'react'
import api from './services/api'
import './App.css'

function App() {
  const [apiStatus, setApiStatus] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Check API health on component mount
    checkApiHealth()
  }, [])

  const checkApiHealth = async () => {
    try {
      const response = await api.get('/health')
      setApiStatus(response.data)
      setLoading(false)
    } catch (error) {
      console.error('API health check failed:', error)
      setApiStatus({ status: 'error', message: 'Failed to connect to API' })
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <header className="app-header">
        <h1>Responsive Web Application</h1>
        <p>React + Flask + PostgreSQL</p>
      </header>
      
      <main className="app-main">
        <section className="status-section">
          <h2>System Status</h2>
          {loading ? (
            <p>Checking system status...</p>
          ) : (
            <div className="status-card">
              <p>
                <strong>API Status:</strong> 
                <span className={`status ${apiStatus?.status === 'healthy' ? 'healthy' : 'error'}`}>
                  {apiStatus?.status || 'Unknown'}
                </span>
              </p>
              {apiStatus?.message && (
                <p><strong>Message:</strong> {apiStatus.message}</p>
              )}
            </div>
          )}
        </section>

        <section className="info-section">
          <h2>Architecture Overview</h2>
          <div className="info-grid">
            <div className="info-card">
              <h3>Frontend</h3>
              <p>React with Vite</p>
              <ul>
                <li>Fast HMR development</li>
                <li>React Router for navigation</li>
                <li>Axios for API calls</li>
              </ul>
            </div>
            <div className="info-card">
              <h3>Backend</h3>
              <p>Flask REST API</p>
              <ul>
                <li>SQLAlchemy ORM</li>
                <li>Flask-Migrate for DB migrations</li>
                <li>CORS enabled</li>
              </ul>
            </div>
            <div className="info-card">
              <h3>Database</h3>
              <p>PostgreSQL</p>
              <ul>
                <li>Relational database</li>
                <li>Docker containerized</li>
                <li>Migration support</li>
              </ul>
            </div>
          </div>
        </section>
      </main>

      <footer className="app-footer">
        <p>Ready for development - Add your features here!</p>
      </footer>
    </div>
  )
}

export default App
