from datetime import date

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Date


class Base(DeclarativeBase):
	...


class Contact(Base):
	__tablename__ = 'contacts'
	id: Mapped[ int ] = mapped_column('id', primary_key=True)
	first_name: Mapped[ str ] = mapped_column('first_name', String(50), index=True, nullable=False)
	last_name: Mapped[ str ] = mapped_column('last_name', String(50), nullable=False)
	email: Mapped[ str ] = mapped_column('email', String(250))
	birthday: Mapped[ date ] = mapped_column('birthday', Date, index=True)
	notes: Mapped[ str | None ] = mapped_column('notes', String(1000))

	phones: Mapped[ list[ "Phone" ] ] = relationship(back_populates='contact', cascade="all, delete-orphan")


class Phone(Base):
	__tablename__ = 'phones'
	id: Mapped[ int ] = mapped_column('id', primary_key=True)
	number: Mapped[ str ] = mapped_column('number', String(13), index=True, nullable=False, unique=True)
	contact_id: Mapped[ int ] = mapped_column('contact_id', ForeignKey('contacts.id'), nullable=False)

	contact: Mapped[ "Contact" ] = relationship(back_populates='phones')
