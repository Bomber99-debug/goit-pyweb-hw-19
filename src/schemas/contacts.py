from datetime import date

from pydantic import BaseModel, EmailStr, Field


class PhoneSchema(BaseModel):
	id: int
	number: str = Field(min_length=9, max_length=13)
	contact_id: int


class PhoneUpdateSchema(PhoneSchema):
	number: str = Field(min_length=9, max_length=13)
	contact_id: int


class PhoneResponseSchema(PhoneSchema):
	id: int
	number: str

	class Config:
		from_attributes = True


class PhoneCreateSchema(BaseModel):
	number: str


class ContactSchema(BaseModel):
	id: int
	first_name: str = Field(min_length=3, max_length=50)
	last_name: str = Field(min_length=3, max_length=50)
	email: EmailStr
	birthday: date
	notes: str | None = Field(max_length=1000)


class ContactUpdateSchema(ContactSchema):
	first_name: str = Field(min_length=3, max_length=50)
	last_name: str = Field(min_length=3, max_length=50)
	email: EmailStr
	birthday: date
	notes: str | None = None


class ContactResponseSchema(BaseModel):
	id: int
	first_name: str
	last_name: str
	email: EmailStr
	birthday: date
	notes: str | None = None
	phones: list[ PhoneResponseSchema ]

	class Config:
		from_attributes = True


class ContactCreateSchema(BaseModel):
	first_name: str
	last_name: str
	email: EmailStr
	birthday: date
	notes: str | None = None
	phones: list[ PhoneCreateSchema ]
