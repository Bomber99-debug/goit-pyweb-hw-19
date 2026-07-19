import select
from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.entity.models import Contact, Phone
from src.repository import contacts as contact_repository
from src.schemas.contacts import (
	ContactSchema,
	ContactUpdateSchema,
	ContactResponseSchema,
	ContactCreateSchema,
	PhoneSchema,
	PhoneUpdateSchema,
	PhoneResponseSchema,
	)

cont = APIRouter(prefix="/contacts", tags=[ "contacts" ])
phone = APIRouter(prefix="/phone", tags=[ "phone" ])


@cont.get("/", response_model=ContactResponseSchema)
async def get_contacts(
		limit: int = Query(default=10, ge=10, le=100),
		offset: int = Query(default=0, ge=0),
		db: AsyncSession = Depends(get_db),
		):
	contacts = await contact_repository.get_contacts(db, limit, offset)
	return contacts


@cont.get("/{cont_id}", response_model=ContactResponseSchema)
async def get_contact_by_id(db: AsyncSession, contact_id: int):
	contacts = await contact_repository.get_contact_by_id(db, contact_id)
	return contacts


@cont.post("/", response_model=ContactCreateSchema, status_code=status.HTTP_201_CREATED)
async def create_contact(db: AsyncSession, body: ContactSchema):
	contact = await contact_repository.create_contact(db, body)
	return contact


@cont.put("/", response_model=ContactResponseSchema)
async def update_contact():
	...


@cont.delete("/", response_model=ContactResponseSchema)
async def delete_contact():
	...
