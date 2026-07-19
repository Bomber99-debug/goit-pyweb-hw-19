from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.entity.models import Contact, Phone
from src.schemas.contacts import (
	ContactSchema,
	ContactUpdateSchema,
	PhoneSchema,
	PhoneUpdateSchema,
	PhoneCreateSchema,
	)


async def get_contacts(db: AsyncSession, skip: int = 0, limit: int = 100):
	stmt = (select(Contact)
	        .options(selectinload(Contact.phones))
	        .offset(skip)
	        .limit(limit))
	contacts = await db.execute(stmt)
	return contacts.scalars().all()


async def get_contact_by_id(db: AsyncSession, contact_id: int):
	stmt = (select(Contact)
	        .filter_by(id=contact_id)
	        .options(selectinload(Contact.phones)))
	contacts = await db.execute(stmt)
	return contacts.scalar_one_or_none()


async def create_contact(db: AsyncSession, body: ContactSchema):
	contact = Contact(**body.model_dump(exclude_unset=True))
	db.add(contact)
	await db.commit()
	await db.refresh(contact)
	return contact


async def update_contact(db: AsyncSession, contact: Contact):
	...


async def delete_contact(db: AsyncSession, contact_id: int):
	...
