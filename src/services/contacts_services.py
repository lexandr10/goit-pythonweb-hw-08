from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from src.controlllers.contacts_controllers import ContactController
from src.schemas.contact_schemas import (
    ContactSchema,
    ContactUpdateSchema,
    ContactResponseSchema,
)


class ContactService:
    def __init__(self, db: AsyncSession):
        self.contact_controller = ContactController(db)

    async def create_contact(self, contact: ContactSchema):
        new_contact = await self.contact_controller.create_contact(contact)
        if not new_contact:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Contact not created"
            )
        return new_contact

    async def get_contacts(self, limit: int = 10, offset: int = 0):
        contacts = await self.contact_controller.get_contacts(limit, offset)
        if not contacts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found"
            )
        return contacts

    async def get_contact_by_id(self, contact_id: int):
        contact = await self.contact_controller.get_contact_by_id(contact_id)
        if not contact:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
            )
        return contact

    async def update_contact(self, contact_id: int, contact: ContactUpdateSchema):
        update = await self.contact_controller.update_contact(contact_id, contact)
        if not update:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
            )
        return update

    async def remove_contact(self, contact_id: int):
        return await self.contact_controller.remove_contact(contact_id)

    async def search_contacts(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
    ):
        contacts = await self.contact_controller.search_contacts(
            first_name, last_name, email
        )
        if not contacts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found"
            )
        return contacts

    async def get_contact_by_birthday(self):
        contacts = await self.contact_controller.get_contact_by_birthday()
        if not contacts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Contacts not found"
            )
        return contacts
