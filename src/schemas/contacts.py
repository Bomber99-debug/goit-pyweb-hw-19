from datetime import date

from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
	first_name: str = Field(min_length=3, max_length=50)
	last_name: str = Field(min_length=3, max_length=50)
	email: EmailStr
	birthday: date
	notes: str = Field(max_length=1000)


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

	class Config:
		from_attributes = True


class PhoneSchema(BaseModel):
	number: str = Field(min_length=10, max_length=13)
	contact_id: int = 1


class PhoneUpdateSchema(ContactSchema):
	number: str = Field(min_length=10, max_length=13)
	contact_id: int = 1


class PhoneResponseSchema(BaseModel):
	number: str
	contact_id: int
