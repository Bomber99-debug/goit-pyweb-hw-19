from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import contacts as contact_repository
from src.schemas.contacts import (
	ContactSchema,
	ContactUpdateSchema,
	ContactResponseSchema,
	PhoneSchema,
	PhoneUpdateSchema,
	PhoneResponseSchema,
	)

cont = APIRouter(prefix="/contacts", tags=[ "contacts" ])
phone = APIRouter(prefix="/phone", tags=[ "phone" ])


@cont.get("/contact", response_model=ContactResponseSchema)
async def get_contact():
	...


@cont.get("/contact", response_model=ContactResponseSchema)
async def get_contact_by_id():
	...


@cont.post("/contact", response_model=ContactResponseSchema)
async def create_contact():
	...


@cont.put("/contact", response_model=ContactResponseSchema)
async def update_contact():
	...


@cont.delete("/contact", response_model=ContactResponseSchema)
async def delete_contact():
	...
