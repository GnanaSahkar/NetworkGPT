
import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    """Application settings."""
    
    #===================
    #project path
    #===================
    
    BASE_DIR: Path = Path(__file__).resolve().parent.parent 
    DATA_DIR: Path = BASE_DIR / "data"
    UPLOAD_DIR: Path = DATA_DIR / "uploads"
    PROCESSED_DIR: Path = DATA_DIR / "processed"
    REPORTS_DIR: Path = DATA_DIR / "reports"
    VECTOR_DB_DIR: Path = DATA_DIR / "vectordb"
    
    #===================
    #API keys
    #===================
    llm_provider = os.getenv("LLM_PROVIDER", "gemini")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY","")
    model_name: str = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    
    #===================
    #LLM settings
    #===================
    TEMPERATURE: float = 0.2
    MAX_OUTPUT_TOKENS: int = 4096
    
settings = Settings()  