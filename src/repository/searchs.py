from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.entity.models import Contact


async def search_first_name(db: AsyncSession, first_name):
	stmt = (select(Contact)
	        .filter_by(first_name=first_name)
	        .options(selectinload(Contact.phones))
	        )
	cont = await db.execute(stmt)
	return cont.scalars().all()


async def search_last_name(db: AsyncSession, last_name):
	stmt = (select(Contact)
	        .filter_by(last_name=last_name)
	        .options(selectinload(Contact.phones))
	        )
	cont = await db.execute(stmt)
	return cont.scalars().all()


async def search_email(db: AsyncSession, email):
	stmt = (select(Contact)
	        .filter_by(email=email)
	        .options(selectinload(Contact.phones))
	        )
	cont = await db.execute(stmt)
	return cont.scalars().all()


async def search_birthday(db: AsyncSession):
	start_date = datetime.today()
	end_date = start_date + timedelta(days=7)

	stmt = (select(Contact)
	        .options(selectinload(Contact.phones))
	        .where(Contact.birthday.between(start_date, end_date))
	        )
	cont = await db.execute(stmt)
	return cont.scalars().all()
