from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import contacts as contact_repository
from src.schemas.contacts import (
	ContactUpdateSchema,
	ContactResponseSchema,
	ContactCreateSchema,
	)

cont = APIRouter(prefix="/contacts", tags=[ "contacts" ])


@cont.get("/", response_model=list[ ContactResponseSchema ])
async def get_contacts(
		limit: int = Query(default=10, ge=10, le=100),
		offset: int = Query(default=0, ge=0),
		db: AsyncSession = Depends(get_db),
		):
	contacts = await contact_repository.contacts(db=db, skip=offset, limit=limit)
	if contacts is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
	return contacts


@cont.get("/{contact_id}", response_model=ContactResponseSchema)
async def get_contact_by_id(db: AsyncSession = Depends(get_db), contact_id: int = Path(ge=1)):
	contacts = await contact_repository.contact_by_id(db=db, contact_id=contact_id)
	if contacts is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
	return contacts


@cont.post("/", response_model=ContactCreateSchema, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactCreateSchema, db: AsyncSession = Depends(get_db)):
	contact = await contact_repository.create_contact(db=db, body=body)
	return contact


@cont.put("/{contact_id}", response_model=ContactUpdateSchema)
async def update_contact(
		body: ContactUpdateSchema,
		contact_id: int = Path(ge=1),
		db: AsyncSession = Depends(get_db),
		):
	contact = await contact_repository.update_contact(
			db=db,
			body=body,
			contact_id=contact_id,
			)
	if contact is None:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
	return contact


@cont.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(db: AsyncSession = Depends(get_db), contact_id: int = Path(ge=1)):
	await contact_repository.delete_contact(db=db, contact_id=contact_id)
