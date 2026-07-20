from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class PhoneBaseSchema(BaseModel):
    """Базові дані телефонного номера."""

    number: str = Field(
        min_length=9,
        max_length=13,
    )
    contact_id: int


class PhoneCreateSchema(PhoneBaseSchema):
    """Дані для створення окремого телефонного номера."""

    ...


class PhoneUpdateSchema(PhoneBaseSchema):
    """Дані для оновлення телефонного номера."""

    ...


class PhoneResponseSchema(PhoneBaseSchema):
    """Дані телефонного номера у відповіді API."""

    model_config = ConfigDict(from_attributes=True)

    id: int


class ContactPhoneCreateSchema(BaseModel):
    """Дані телефонного номера під час створення контакту."""

    number: str


class ContactBaseSchema(BaseModel):
    """Базові дані контакту."""

    first_name: str = Field(
        min_length=3,
        max_length=50,
    )
    last_name: str = Field(
        min_length=3,
        max_length=50,
    )
    email: EmailStr
    birthday: date
    notes: str | None = Field(max_length=1000)


class ContactUpdateSchema(ContactBaseSchema):
    """Дані для оновлення контакту."""

    notes: str | None = None


class ContactResponseSchema(BaseModel):
    """Дані контакту у відповіді API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    birthday: date
    notes: str | None = None
    phones: list[PhoneResponseSchema]


class ContactCreateSchema(BaseModel):
    """Дані для створення контакту."""

    first_name: str
    last_name: str
    email: EmailStr
    birthday: date
    notes: str | None = None
    phones: list[ContactPhoneCreateSchema]
