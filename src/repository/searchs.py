from datetime import date, timedelta

from sqlalchemy import select, func
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
	today = date.today()
	next_7_days = [ today + timedelta(days=i) for i in range(8) ]
	target_days = [ d.strftime('%m-%d') for d in next_7_days ]

	stmt = (select(Contact)
	        .options(selectinload(Contact.phones))
	        .where(func.to_char(Contact.birthday, 'MM-DD').in_(target_days))
	        )
	cont = await db.execute(stmt)
	return cont.scalars().all()
