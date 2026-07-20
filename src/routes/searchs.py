from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import searchs as search_repository
from src.schemas.contacts import ContactResponseSchema

search = APIRouter(prefix="/searchs", tags=[ "search" ])


@search.get("/", response_model=list[ContactResponseSchema])
async def search_contacts(
		query: Annotated[
			str,
			Query(
				min_length=1,
				max_length=250,
				description="Ім'я, прізвище або email контакту",
				),
			],
		db: AsyncSession = Depends(get_db),
		):
	contacts = await search_repository.search_contacts(
		db=db,
		query=query,
		)

	return contacts


@search.get("/birthday/", response_model=list[ ContactResponseSchema ])
async def search_birthday(db: AsyncSession = Depends(get_db)):
	searching = await search_repository.search_birthday(db=db)
	return searching
