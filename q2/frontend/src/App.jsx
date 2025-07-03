import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';
import Login from './pages/Login';
import Register from './pages/Register';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          {/* Public routes */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          
          {/* Protected routes */}
          <Route
            path="/products"
            element={
              <ProtectedRoute>
                <div>Products Page (Coming Soon)</div>
              </ProtectedRoute>
            }
          />
          
          {/* Redirect root to products or login */}
          <Route
            path="/"
            element={<Navigate to="/products" replace />}
          />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
