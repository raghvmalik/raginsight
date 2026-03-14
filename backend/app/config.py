from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "RAGInsight"
    VERSION: str = "1.0.0"

    OPENAI_API_KEY: str

    DATABASE_URL: str = "sqlite:///./rag.db"
    VECTOR_STORE_PATH: str = "./vector_db"

    class Config:
        env_file = ".env"


settings = Settings()
