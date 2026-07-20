from datetime import date, timedelta

from sqlalchemy import or_, select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.entity.models import Contact


async def search_contacts(
		db: AsyncSession,
		query: str,
		):
	stmt = (
		select(Contact)
		.options(selectinload(Contact.phones))
		.where(
			or_(
				Contact.first_name.ilike(f"%{query}%"),
				Contact.last_name.ilike(f"%{query}%"),
				Contact.email.ilike(f"%{query}%"),
				)
			)
		)

	result = await db.execute(stmt)

	return result.scalars().all()


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
