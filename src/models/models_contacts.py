from datetime import date


from sqlalchemy import String, Date, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.conf.constants import NAME_MAX_LENGTH, NAME_MIN_LENGTH, MAX_PHONE_LENGTH


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH), nullable=False)
    last_name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH), nullable=False)
    email: Mapped[str] = mapped_column(
        String(NAME_MAX_LENGTH), nullable=False, unique=True
    )
    phone: Mapped[str] = mapped_column(
        String(MAX_PHONE_LENGTH), nullable=False, unique=True
    )
    birthday: Mapped[date] = mapped_column(
        Date, default=func.current_date(), nullable=False
    )
    additional_data: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH))

    created_at: Mapped[date] = mapped_column(Date, default=func.current_date())
