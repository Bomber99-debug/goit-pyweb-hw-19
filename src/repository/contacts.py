from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.entity.models import Contact, Phone
from src.schemas.contacts import (
	ContactUpdateSchema,
	ContactCreateSchema,
	)


async def contacts(db: AsyncSession, skip: int = 0, limit: int = 100):
	stmt = (select(Contact)
	        .options(selectinload(Contact.phones))
	        .offset(skip)
	        .limit(limit))
	cont = await db.execute(stmt)
	return cont.scalars().all()


async def contact_by_id(db: AsyncSession, phone_id: int):
	stmt = (select(Contact)
	        .filter_by(id=phone_id)
	        .options(selectinload(Contact.phones))
	        )
	cont = await db.execute(stmt)
	return cont.scalar_one_or_none()


async def create_contact(db: AsyncSession, body: ContactCreateSchema):
	data = body.model_dump(exclude={"phones"})
	phones = [
			Phone(**phone.model_dump())
			for phone in body.phones
			]
	contact = Contact(**data, phones=phones)
	db.add(contact)
	await db.commit()
	return contact


async def update_contact(db: AsyncSession, body: ContactUpdateSchema, contact_id: int):
	stmt = select(Contact).filter_by(id=contact_id)
	result = await db.execute(stmt)
	updated_contact = result.scalar_one_or_none()
	if updated_contact:
		updated_contact.first_name = body.first_name
		updated_contact.last_name = body.last_name
		updated_contact.email = body.email
		updated_contact.birthday = body.birthday
		updated_contact.notes = body.notes
		await db.commit()
		await db.refresh(updated_contact)
	return updated_contact

async def delete_contact(db: AsyncSession, contact_id: int):
	stmt = select(Contact).filter_by(id=contact_id)
	result = await db.execute(stmt)
	deleted_contact = result.scalar_one_or_none()
	if deleted_contact:
		await db.delete(deleted_contact)
		await db.commit()
	return deleted_contact
