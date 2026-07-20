from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import searchs as search_repository
from src.schemas.contacts import ContactResponseSchema

search = APIRouter(prefix="/searchs", tags=[ "search" ])


@search.get("/first_name/{first_name}", response_model=list[ ContactResponseSchema ])
async def search_first_name(first_name: str, db: AsyncSession = Depends(get_db)):
	searching = await search_repository.search_first_name(db=db, first_name=first_name)
	if searching is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone not found")
	return searching


@search.get("/last_name/{last_name}", response_model=list[ ContactResponseSchema ])
async def search_last_name(last_name: str, db: AsyncSession = Depends(get_db)):
	searching = await search_repository.search_last_name(db=db, last_name=last_name)
	if searching is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone not found")
	return searching


@search.get("/email/{email}", response_model=list[ ContactResponseSchema ])
async def search_email(email: str, db: AsyncSession = Depends(get_db)):
	searching = await search_repository.search_email(db=db, email=email)
	if searching is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone not found")
	return searching


@search.get("/birthday/", response_model=list[ ContactResponseSchema ])
async def search_birthday(db: AsyncSession = Depends(get_db)):
	searching = await search_repository.search_birthday(db=db)
	if searching is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone not found")
	return searching
