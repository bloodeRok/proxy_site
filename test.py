import asyncio

from app.services import RequestService

asyncio.run(RequestService().add_requests_to_db())
