# AI-Powered Product Recommendation System

A full-stack application featuring user authentication and AI-powered product recommendations.

## Project Structure

```
project/
├── frontend/         # React + Vite frontend
├── backend/          # FastAPI backend
```

## Setup Instructions

### Frontend Setup
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start development server:
   ```bash
   npm run dev
   ```
   Frontend will be available at http://localhost:5173

### Backend Setup
1. Navigate to backend directory:
   ```bash
   cd backend
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create .env file with following variables:
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/product_recommendation
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
5. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
   Backend API will be available at http://localhost:8000

## Features
- User authentication
- Product catalog
- AI-powered recommendations
- User interaction tracking 