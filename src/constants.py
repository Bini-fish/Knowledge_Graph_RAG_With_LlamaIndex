"""Configuration: set these in .env (copy from .env.example) or edit the values below."""
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

neo4j_username = os.getenv("NEO4J_USERNAME", "enter-username")
neo4j_password = os.getenv("NEO4J_PASSWORD", "enter-password")
neo4j_url = os.getenv("NEO4J_URL", "enter-url")

google_api = os.getenv("GOOGLE_API_KEY", "enterapi_key")
search_engine_id = os.getenv("SEARCH_ENGINE_ID", "enter_id")
open_ai_key = os.getenv("OPENAI_API_KEY", "enter_openai_key")
