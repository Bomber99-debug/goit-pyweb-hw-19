from datetime import date

from pydantic import BaseModel, EmailStr, Field


class PhoneSchema(BaseModel):
	number: str = Field(min_length=10, max_length=13)
	contact_id: int = 1


class PhoneUpdateSchema(PhoneSchema):
	number: str = Field(min_length=10, max_length=13)
	contact_id: int = 1


class PhoneResponseSchema(PhoneSchema):
	number: str


class PhoneCreateSchema(BaseModel):
	number: str


class ContactSchema(BaseModel):
	first_name: str = Field(min_length=3, max_length=50)
	last_name: str = Field(min_length=3, max_length=50)
	email: EmailStr
	birthday: date
	notes: str = Field(max_length=1000)
	number: list[ PhoneCreateSchema ]


class ContactUpdateSchema(ContactSchema):
	first_name: str = Field(min_length=3, max_length=50)
	last_name: str = Field(min_length=3, max_length=50)
	email: EmailStr
	birthday: date
	notes: str = Field(max_length=1000)


class ContactResponseSchema(BaseModel):
	id: int = 1
	first_name: str
	last_name: str
	email: EmailStr
	birthday: date
	number: list[ PhoneResponseSchema ]

	class Config:
		from_attributes = True


class ContactCreateSchema(BaseModel):
	first_name: str
	last_name: str
	email: EmailStr
	birthday: date
	number: list[ PhoneCreateSchema ]
