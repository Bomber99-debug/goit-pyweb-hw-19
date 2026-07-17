from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Contact, Phone
from src.schemas.contacts import ContactSchema, ContactUpdateSchema, PhoneSchema, PhoneUpdateSchema


async def get_contacts(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[ Contact ]:
	...


async def get_contact_by_id(db: AsyncSession, contact_id: int) -> Contact:
	...


async def create_contact(db: AsyncSession, contact: Contact) -> Contact:
	...


async def update_contact(db: AsyncSession, contact: Contact) -> Contact:
	...


async def delete_contact(db: AsyncSession, contact_id: int) -> None:
	...
