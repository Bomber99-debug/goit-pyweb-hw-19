from src.conf.connect_settings import user, db_name, password, host, port

class Config:
	DB_URL = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"


config = Config()
