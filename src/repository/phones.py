from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Phone
from src.schemas.contacts import PhoneUpdateSchema, PhoneSchema


async def phones(db: AsyncSession, skip: int = 0, limit: int = 100):
	stmt = (select(Phone)
	        .offset(skip)
	        .limit(limit))
	numbers = await db.execute(stmt)
	return numbers.scalars().all()


async def phone_by_id(db: AsyncSession, phone_id: int):
	stmt = (select(Phone)
	        .filter_by(id=phone_id)
	        )
	number = await db.execute(stmt)
	return number.scalar_one_or_none()

async def create_phone(db: AsyncSession, body: PhoneSchema):
	phone = Phone(**body.model_dump(exclude_unset=True))
	db.add(phone)
	await db.commit()
	return phone

async def update_phone(db: AsyncSession, body: PhoneUpdateSchema, phone_id: int):
	stmt = select(Phone).filter_by(id=phone_id)
	result = await db.execute(stmt)
	updated_number = result.scalar_one_or_none()
	if updated_number:
		updated_number.number = body.number
		updated_number.contact_id = body.contact_id
		await db.commit()
		await db.refresh(updated_number)
	return updated_number


async def delete_phone(db: AsyncSession, phone_id: int):
	stmt = select(Phone).filter_by(id=phone_id)
	result = await db.execute(stmt)
	deleted_phone = result.scalar_one_or_none()
	if deleted_phone:
		await db.delete(deleted_phone)
		await db.commit()
	return deleted_phone
