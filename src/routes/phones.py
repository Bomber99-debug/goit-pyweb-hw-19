from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import phones as phones_repository
from src.schemas.contacts import (
	PhoneResponseSchema,
	PhoneUpdateSchema,
	)

phone = APIRouter(prefix="/phone", tags=[ "phone" ])


@phone.get("/", response_model=list[ PhoneResponseSchema ])
async def get_phones(
		limit: int = Query(default=10, ge=10, le=100),
		offset: int = Query(default=0, ge=0),
		db: AsyncSession = Depends(get_db),
		):
	phones = await phones_repository.phones(db=db, skip=offset, limit=limit)
	if phones is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone not found")
	return phones


@phone.get("/{contact_id}", response_model=PhoneResponseSchema)
async def get_contact_by_id(db: AsyncSession = Depends(get_db), contact_id: int = Path(ge=1)):
	phones = await phones_repository.phone_by_id(db=db, contact_id=contact_id)
	if phones is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone not found")
	return phones


@phone.put("/{phone_id}", response_model=PhoneUpdateSchema)
async def update_phone(
		body: PhoneUpdateSchema,
		phone_id: int = Path(ge=1),
		db: AsyncSession = Depends(get_db),
		):
	number = await phones_repository.update_phone(
			db=db,
			body=body,
			phone_id=phone_id,
			)
	if number is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
	return number


@phone.delete("/{phone_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(db: AsyncSession = Depends(get_db), phone_id: int = Path(ge=1)):
	await phones_repository.delete_phone(db=db, phone_id=phone_id)
