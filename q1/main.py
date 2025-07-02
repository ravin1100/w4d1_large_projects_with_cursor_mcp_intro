import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv
import markdown
import re

# Load environment variables
load_dotenv()

# Configure Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = FastAPI(title="MCP Q&A Chatbot")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    text: str

def load_knowledge_base():
    with open("knowledge_base.md", "r", encoding="utf-8") as f:
        return f.read()

def search_knowledge_base(query: str, knowledge_base: str) -> Optional[str]:
    # Convert query to lowercase for case-insensitive matching
    query_lower = query.lower()
    
    # Split knowledge base into sections
    sections = re.split(r'\n##? ', knowledge_base)
    
    relevant_sections = []
    for section in sections:
        if section.lower().find(query_lower) != -1:
            relevant_sections.append(section.strip())
    
    if relevant_sections:
        return "\n\n".join(relevant_sections)
    return None

@app.post("/api/ask")
async def ask_question(question: Question):
    try:
        # Load knowledge base
        knowledge_base = load_knowledge_base()
        
        # Search for relevant information in knowledge base
        context = search_knowledge_base(question.text, knowledge_base)
        
        if context:
            # If relevant information found in knowledge base, use it to generate response
            prompt = f"""Based on the following context about MCP (Model Context Protocol), 
            please answer the question: {question.text}\n\nContext:\n{context}"""
        else:
            # If no relevant information found, use Gemini to generate response
            prompt = f"""You are an expert on Model Context Protocol (MCP). 
            Please answer the following question about MCP: {question.text}
            Provide a detailed and technical answer."""
        
        # Generate response using Gemini
        response = model.generate_content(prompt)
        
        return {
            "answer": response.text,
            "source": "knowledge_base" if context else "gemini"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files after API routes
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to MCP Q&A Chatbot API"} 