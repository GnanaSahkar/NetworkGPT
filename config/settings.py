
import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv
import dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    """Application settings."""
    
    #===================
    #project path
    #===================
    
    BASE_DIR: Path = Path(__file__).resolve().parent.parent 
    DTA_DIR: Path = BASE_DIR / "data"
    UPLOAD_DIR: Path = BASE_DIR / "uploads"
    PROCESSED_DIR: Path = BASE_DIR / "processed"
    REPORTS_DIR: Path = BASE_DIR / "reports"
    VECTOR_DB_DIR: Path = BASE_DIR / "vector_db"
    
    #===================
    #API keys
    #===================
    GENAI_API_KEY: str = os.getenv("GENAI_API_KEY","")
    model_name: str = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    
    #===================
    #LLM settings
    #===================
    TEMPARATURE: float = 0.2
    MAX_OUTPUT_TOKENS: int = 4096
    
settings = Settings()  