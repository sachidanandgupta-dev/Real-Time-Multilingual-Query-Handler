from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from translator import detect_language, translate_text
from llm_handler import get_response

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    message: str

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Backend is running"}

@app.post("/query")
def handle_query(query: Query):
    try:
        user_text = query.message

        # Step 1: detect language
        lang = detect_language(user_text)

        # Step 2: translate to English
        english_text = translate_text(user_text, target="en")

        # Step 3: get LLM response
        response = get_response(english_text)

        # Step 4: translate back
        final_response = translate_text(response, target=lang)

        return {
            "detected_language": lang,
            "response": final_response
        }
    except Exception as e:
        return {
            "error": str(e),
            "message": "An error occurred while processing your query. Make sure your OpenAI API key is set correctly."
        }