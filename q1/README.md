# MCP Q&A Chatbot

A specialized chatbot that answers questions about Model Context Protocol (MCP). The chatbot uses a combination of a local knowledge base and the Google Gemini API to provide accurate and detailed responses about MCP concepts, implementation, best practices, and troubleshooting.

![MCP Q&A Chatbot Interface](https://i.imgur.com/placeholder.png)
(Note: Replace the placeholder.png with an actual screenshot of your UI)

## Features

- 🧠 Comprehensive MCP knowledge base
- 🤖 Intelligent question answering using both local knowledge and Gemini AI
- 💻 Modern, responsive web interface
- ⚡ Real-time chat interaction
- 📝 Source attribution for answers (knowledge base vs Gemini)
- 🔄 Automatic fallback to Gemini AI when local knowledge is insufficient

## Project Structure

```
mcp-qa-chatbot/
├── static/
│   └── index.html         # Frontend UI
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore rules
├── knowledge_base.md     # MCP documentation and knowledge
├── main.py              # FastAPI backend server
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Modern web browser
- pip (Python package installer)

## Environment Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd mcp-qa-chatbot
```

2. Create a virtual environment and activate it:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
# Required
GOOGLE_API_KEY=your_gemini_api_key_here

# Optional
PORT=8000
HOST=0.0.0.0
```

## Configuration

### Environment Variables (.env)

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| GOOGLE_API_KEY | Your Google Gemini API key | Yes | - |
| PORT | Server port number | No | 8000 |
| HOST | Server host address | No | 127.0.0.1 |

To get a Google Gemini API key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or select a project
3. Generate an API key
4. Copy the key to your `.env` file

## Running the Application

1. Ensure your virtual environment is activated
2. Start the server:
```bash
uvicorn main:app --reload
```
3. Open your browser and navigate to `http://localhost:8000`

## API Endpoints

| Endpoint | Method | Description | Request Body | Response |
|----------|---------|-------------|--------------|----------|
| `/` | GET | Serves the main chat interface | - | HTML |
| `/api/ask` | POST | Processes questions | `{ "text": "string" }` | `{ "answer": "string", "source": "string" }` |

## How It Works

1. **Knowledge Base Search**
   - Questions are first searched in the local knowledge base
   - Uses semantic matching to find relevant sections
   - Returns context-aware responses

2. **Gemini AI Fallback**
   - If no relevant information is found locally
   - Uses Gemini 1.5 Flash model for fast responses
   - Provides technical, MCP-focused answers

3. **Response Attribution**
   - Each response includes its source
   - "knowledge_base" for local matches
   - "gemini" for AI-generated responses

## Contributing

1. Fork the repository
2. Create a feature branch
```bash
git checkout -b feature/amazing-feature
```
3. Commit your changes
```bash
git commit -m 'Add amazing feature'
```
4. Push to the branch
```bash
git push origin feature/amazing-feature
```
5. Open a Pull Request

## Development Notes

- The knowledge base (`knowledge_base.md`) can be extended with new MCP information
- Frontend uses Tailwind CSS for styling
- Backend uses FastAPI for high performance
- Gemini 1.5 Flash model is used for faster response times

## Troubleshooting

Common issues and solutions:

1. **API Key Issues**
   - Ensure `.env` file exists in root directory
   - Verify API key is correctly copied
   - Check for any whitespace in the key

2. **Server Won't Start**
   - Verify port 8000 is not in use
   - Ensure all dependencies are installed
   - Check virtual environment is activated

3. **No Response from Bot**
   - Check browser console for errors
   - Verify API endpoint is correct
   - Ensure knowledge base file exists

## License

MIT License - see LICENSE file for details

## Acknowledgments

- FastAPI for the excellent web framework
- Google Gemini for AI capabilities
- Tailwind CSS for the UI components 