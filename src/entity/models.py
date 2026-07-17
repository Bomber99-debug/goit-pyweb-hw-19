from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationships
from sqlalchemy import ForeignKey, String, Date

class Base(DeclarativeBase):
	...

class Contact(Base):
	__tablename__ = 'contacts'
	id: Mapped = mapped_column('id', primary_key=True)
	first_name: Mapped = mapped_column('first_name', String(50), index=True, nullable=False)
	last_name: Mapped = mapped_column('last_name', String(50))
	email: Mapped = mapped_column('email', String(250))
	birthday: Mapped = mapped_column('birthday', Date, index=True)
	notes: Mapped = mapped_column('notes', String(1000))

	telephones: Mapped[list["Telephone"]] = relationships(back_populates='contact', cascade="all, delete-orphan")

class Telephone(Base):
	__tablename__ = 'telephones'
	telephone: Mapped = mapped_column('telephone', String(13), index=True, nullable=False)

	contact_id: Mapped = mapped_column('contact_id', ForeignKey('contacts.id'))

	contact: Mapped["Contact"] = relationships(back_populates='telephones')