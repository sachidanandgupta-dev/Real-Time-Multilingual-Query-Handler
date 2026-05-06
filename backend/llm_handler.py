import os
from dotenv import load_dotenv

load_dotenv()

def get_response(prompt):
    """
    Mock LLM responses for testing without API quota.
    Replace with real OpenAI when account is set up with billing.
    """
    print(f"[LLM] Processing prompt (MOCK MODE): {prompt[:50]}...")
    
    # Specific topic responses (check these first)
    specific_responses = {
        "sql": "SQL (Structured Query Language) is a standardized programming language used for managing and querying relational databases. It allows you to create, read, update, and delete data in databases. SQL is used with database systems like MySQL, PostgreSQL, SQL Server, and Oracle.",
        "database": "A database is an organized collection of structured data stored electronically in a computer system. It uses a Database Management System (DBMS) to manage access and modifications to the data. Databases are used to store information efficiently and retrieve it quickly.",
        "api": "An API (Application Programming Interface) is a set of protocols and tools for building software applications. It allows different software applications to communicate with each other and share data. APIs define the methods and data formats that applications can use to request and exchange information.",
        "python": "Python is a versatile, high-level programming language known for its simplicity and readability. It's widely used in web development, data science, artificial intelligence, machine learning, automation, and scripting. Python emphasizes code readability and allows developers to write programs with fewer lines of code.",
        "javascript": "JavaScript is a programming language primarily used for creating interactive web pages and web applications. It runs in web browsers and allows you to add interactivity, animations, and dynamic content to websites. JavaScript is also used in server-side development with Node.js.",
        "machine learning": "Machine Learning is a subset of Artificial Intelligence where computer systems learn from data without being explicitly programmed. The system improves its performance through experience. Machine learning is used in recommendation systems, image recognition, natural language processing, and predictive analytics.",
        "artificial intelligence": "Artificial Intelligence (AI) refers to computer systems designed to perform tasks that typically require human intelligence. This includes learning from experience, recognizing patterns, understanding language, and making decisions. AI applications include chatbots, recommendation systems, autonomous vehicles, and image recognition.",
        "web development": "Web Development is the process of building and maintaining websites and web applications. It involves frontend development (user interface), backend development (server logic), and database management. Technologies include HTML, CSS, JavaScript, Python, Node.js, and various frameworks.",
        "cloud computing": "Cloud Computing is the delivery of computing services over the internet, including servers, storage, databases, and software. Instead of owning physical hardware, users access computing resources on demand from cloud providers like AWS, Google Cloud, and Azure.",
    }
    
    # Generic responses (fallback)
    generic_responses = {
        "what is": "That's a great question! Let me provide you with detailed information about that topic.",
        "explain": "I'd be happy to explain that for you in detail.",
        "tell me": "I'd be happy to tell you more about that topic.",
        "hello": "Hello! How can I help you today?",
        "how are you": "I'm doing well, thank you for asking! How can I assist you?",
        "help": "Of course! I'm here to help. What do you need assistance with?",
    }
    
    # Check specific topics first (case-insensitive)
    prompt_lower = prompt.lower()
    for keyword, response in specific_responses.items():
        if keyword in prompt_lower:
            print(f"[LLM] Matched specific keyword: {keyword}")
            return response
    
    # Then check generic phrases
    for keyword, response in generic_responses.items():
        if keyword in prompt_lower:
            print(f"[LLM] Matched generic keyword: {keyword}")
            return response
    
    # Default response
    default = f"Thank you for your question about '{prompt}'. That's an interesting topic! Here are some key points: I can help you understand various topics in technology, programming, and data science. Feel free to ask about specific subjects like SQL, Python, APIs, Machine Learning, or Cloud Computing."
    print(f"[LLM] Using default response")
    return default