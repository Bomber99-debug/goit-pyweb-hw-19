from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.routes import contacts
from src.routes import phones

app = FastAPI()

app.include_router(contacts.cont)
app.include_router(phones.phone)


@app.get("/")
async def root():
	return { "message": "Hello World" }


@app.get("/contacts/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
	try:
		# Make request
		result = await db.execute(text("SELECT 1"))
		result = result.fetchone()
		if result is None:
			raise HTTPException(status_code=500, detail="Database is not configured correctly")
		return { "message": "Welcome to FastAPI! APP Contacts" }
	except Exception as e:
		print(e)
		raise HTTPException(status_code=500, detail="Error connecting to the database")

@app.get("/phone/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
	try:
		# Make request
		result = await db.execute(text("SELECT 1"))
		result = result.fetchone()
		if result is None:
			raise HTTPException(status_code=500, detail="Database is not configured correctly")
		return { "message": "Welcome to FastAPI! APP Phone!" }
	except Exception as e:
		print(e)
		raise HTTPException(status_code=500, detail="Error connecting to the database")