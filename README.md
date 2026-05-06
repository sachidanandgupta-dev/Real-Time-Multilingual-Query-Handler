# Real-Time Multilingual Query System

A full-stack application that provides real-time multilingual query processing and translation capabilities. The system combines a Python backend with LLM integration and a React frontend for seamless user interaction.

## Features

- 🌍 **Multilingual Support**: Process queries in multiple languages
- ⚡ **Real-Time Processing**: Fast query handling and responses
- 🤖 **LLM Integration**: Powered by advanced language models
- 🔄 **Translation**: Automatic language translation capabilities
- 💻 **Modern UI**: Responsive React-based frontend
- 📡 **RESTful API**: Clean backend API architecture

## Project Structure

```
Real-Time Multilingual Query System/
├── backend/
│   ├── main.py              # Flask/FastAPI application entry point
│   ├── llm_handler.py       # LLM integration and handling
│   ├── translator.py        # Translation utilities
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── package.json         # Node.js dependencies
│   ├── public/
│   │   └── index.html       # HTML entry point
│   └── src/
│       ├── index.js         # React entry point
│       ├── App.js           # Main App component
│       ├── App.css          # Application styles
│       └── api.js           # API client
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 14+** (for frontend)
- **npm** or **yarn** (package manager)

## Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the backend server:
```bash
python main.py
```

The backend will start on `http://localhost:5000` (or configured port)

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will open at `http://localhost:3000`

## Usage

1. Open the application in your browser at `http://localhost:3000`
2. Enter your query in the input field
3. Select your preferred language
4. Submit the query to receive real-time responses
5. View translations and processed results

## API Endpoints

Check the backend documentation for available API endpoints and parameters.

## Technologies Used

### Backend
- Python
- Flask/FastAPI
- LLM libraries (e.g., OpenAI, HuggingFace)
- Translation libraries

### Frontend
- React
- CSS
- Axios/Fetch API

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue in the repository.
