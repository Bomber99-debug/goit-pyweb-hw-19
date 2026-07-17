from datetime import date

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Date


class Base(DeclarativeBase):
	...


class Contact(Base):
	__tablename__ = 'contacts'
	id: Mapped[ int ] = mapped_column('id', primary_key=True)
	first_name: Mapped[ str ] = mapped_column('first_name', String(50), index=True, nullable=False)
	last_name: Mapped[ str | None ] = mapped_column('last_name', String(50))
	email: Mapped[ str ] = mapped_column('email', String(250))
	birthday: Mapped[ Date ] = mapped_column('birthday', Date, index=True)
	notes: Mapped[ str | None ] = mapped_column('notes', String(1000))

	telephones: Mapped[ list[ "Telephone" ] ] = relationship(back_populates='contact', cascade="all, delete-orphan")


class Telephone(Base):
	__tablename__ = 'telephones'
	id: Mapped[ int ] = mapped_column('id', primary_key=True)
	telephone: Mapped[ str ] = mapped_column('telephone', String(13), index=True, nullable=False)

	contact_id: Mapped[ int ] = mapped_column('contact_id', ForeignKey('contacts.id'), nullable=False)

	contact: Mapped[ "Contact" ] = relationship(back_populates='telephones')
